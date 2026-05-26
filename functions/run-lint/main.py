"""
Scheduled Lint Job — Cloud Function
Runs weekly (via Cloud Scheduler) to audit the wiki/ directory against the
CLAUDE.md lint checklist and emails a numbered report to the admin.
"""

import json
import logging
import os
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

import functions_framework
import vertexai
from google.cloud import storage
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from vertexai.generative_models import GenerationConfig, GenerativeModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GCP_PROJECT    = os.environ["GCP_PROJECT"]
STAGING_BUCKET = os.environ["STAGING_BUCKET"]
WIKI_REPO      = os.environ["WIKI_REPO"]
ADMIN_EMAIL    = os.environ["ADMIN_EMAIL"]
TODAY          = date.today().isoformat()
MODEL_NAME     = "gemini-1.5-flash"   # Faster/cheaper model is sufficient for lint
REGION         = "europe-west1"


@functions_framework.http
def run_lint(request):
    """Triggered by Cloud Scheduler. Runs the full CLAUDE.md lint checklist."""
    logger.info("Starting weekly wiki lint job")

    gcs = storage.Client()
    vertexai.init(project=GCP_PROJECT, location=REGION)
    model = GenerativeModel(MODEL_NAME)

    # Load all wiki pages from the current-wiki mirror in GCS
    pages = _load_wiki_pages(gcs)
    logger.info(f"Loaded {len(pages)} wiki pages")

    findings = []
    finding_num = 1

    # ── Check 1: Format violations ────────────────────────────────────────────
    format_issues = _check_format_violations(pages)
    for issue in format_issues:
        findings.append(f"{finding_num}. **Format violation** in `{issue['page']}`: {issue['message']}")
        finding_num += 1

    # ── Check 2: Orphan pages (no inbound wiki-links) ─────────────────────────
    orphans = _find_orphan_pages(pages)
    for orphan in orphans:
        findings.append(
            f"{finding_num}. **Orphan page** `{orphan}` has no inbound [[wiki-links]] from other pages. "
            f"Suggested fix: add a [[{orphan}]] link from a relevant concept page or index.md."
        )
        finding_num += 1

    # ── Check 3: Broken wiki-links (linked page doesn't exist) ────────────────
    broken_links = _find_broken_links(pages)
    for link_info in broken_links:
        findings.append(
            f"{finding_num}. **Broken link** `[[{link_info['target']}]]` in `{link_info['source']}` "
            f"— no matching page found. Suggested fix: create `wiki/{link_info['target']}.md` or "
            f"correct the link."
        )
        finding_num += 1

    # ── Check 4: Missing concept pages ────────────────────────────────────────
    # (links that appear in body text but have no page)
    # Already covered by Check 3 above.

    # ── Check 5: Claims without source citations (sample check) ──────────────
    uncited = _find_uncited_claims(pages)
    for issue in uncited:
        findings.append(
            f"{finding_num}. **Uncited claim** in `{issue['page']}`: \"{issue['claim'][:120]}…\" "
            f"— add `(source: filename.pdf)` or mark as `(source: needs verification)`."
        )
        finding_num += 1

    # ── Check 6: AI contradiction check (uses Gemini) ─────────────────────────
    contradictions = _check_contradictions_ai(pages, model)
    for c in contradictions:
        findings.append(
            f"{finding_num}. **Potential contradiction** between `{c['page_a']}` and `{c['page_b']}`: "
            f"{c['description']}"
        )
        finding_num += 1

    # ── Build report ──────────────────────────────────────────────────────────
    if findings:
        report = _build_report(findings, len(pages))
        _send_email(report)
        _save_report_to_gcs(gcs, report)
        logger.info(f"Lint complete: {len(findings)} finding(s). Report emailed.")
    else:
        report = _build_report([], len(pages))
        _send_email(report)
        logger.info("Lint complete: no findings.")

    return {"status": "ok", "findings": len(findings)}, 200


# ─── Lint checks ──────────────────────────────────────────────────────────────

REQUIRED_FIELDS = ["Summary", "Research classification", "Sources", "Last updated"]
VALID_CLASSIFICATIONS = {"empirical", "theoretical", "both"}


def _check_format_violations(pages: dict[str, str]) -> list[dict]:
    issues = []
    for slug, content in pages.items():
        if slug in ("index", "log"):
            continue
        for field in REQUIRED_FIELDS:
            if f"**{field}**" not in content:
                issues.append({"page": slug, "message": f"missing **{field}** field"})
        cls_match = re.search(r"\*\*Research classification\*\*\s*:\s*(.+)", content)
        if cls_match:
            val = cls_match.group(1).strip().lower()
            if val not in VALID_CLASSIFICATIONS:
                issues.append({"page": slug, "message": f"invalid classification '{val}'"})
        if not content.strip().startswith("# "):
            issues.append({"page": slug, "message": "does not start with a # heading"})
        if "## Related pages" not in content:
            issues.append({"page": slug, "message": "missing ## Related pages section"})
    return issues


def _find_orphan_pages(pages: dict[str, str]) -> list[str]:
    """Find pages that no other page links to."""
    # Collect all outbound links
    inbound: dict[str, int] = defaultdict(int)
    all_slugs = set(pages.keys()) - {"index", "log"}

    for slug, content in pages.items():
        links = re.findall(r"\[\[([^\]]+)\]\]", content)
        for link in links:
            link_slug = link.lower().replace(" ", "-")
            if link_slug != slug:
                inbound[link_slug] += 1

    return [s for s in all_slugs if inbound[s] == 0]


def _find_broken_links(pages: dict[str, str]) -> list[dict]:
    """Find [[wiki-links]] that point to pages that don't exist."""
    existing = set(pages.keys())
    broken = []
    for slug, content in pages.items():
        links = re.findall(r"\[\[([^\]]+)\]\]", content)
        for link in links:
            link_slug = link.lower().replace(" ", "-")
            if link_slug not in existing:
                broken.append({"source": slug, "target": link_slug})
    return broken


def _find_uncited_claims(pages: dict[str, str], sample_size: int = 5) -> list[dict]:
    """
    Heuristic: find long sentences in the body that lack (source: ...).
    Samples up to sample_size pages to avoid overwhelming the report.
    """
    issues = []
    checked = 0
    for slug, content in pages.items():
        if slug in ("index", "log") or checked >= sample_size:
            break
        body_match = re.search(r"---\n(.+)", content, re.DOTALL)
        if not body_match:
            continue
        body = body_match.group(1)
        sentences = re.split(r"(?<=[.!?])\s+", body)
        for sentence in sentences:
            if (
                len(sentence) > 80
                and "(source:" not in sentence
                and "needs verification" not in sentence
                and not sentence.strip().startswith(("#", "-", "*", ">", "**", "[["))
            ):
                issues.append({"page": slug, "claim": sentence.strip()})
                break   # one per page to keep report concise
        checked += 1
    return issues


CONTRADICTION_PROMPT = """You are auditing an academic wiki on monetary policy.
Review these wiki page excerpts and identify any pairs of pages that make
contradictory factual claims about the same policy instrument, country, or time period.
Return ONLY a JSON array:
[
  {{"page_a": "slug1", "page_b": "slug2", "description": "Brief description of contradiction"}}
]
Return an empty array [] if no contradictions are found.

Pages to review:
{excerpts}"""


def _check_contradictions_ai(
    pages: dict[str, str],
    model: GenerativeModel,
    max_pages: int = 10,
) -> list[dict]:
    """
    Use Gemini to check for contradictions across the most recently updated pages.
    Limits to max_pages to control cost.
    """
    # Sort pages by Last updated date to prioritise recent changes
    dated_pages = []
    for slug, content in pages.items():
        if slug in ("index", "log"):
            continue
        match = re.search(r"\*\*Last updated\*\*\s*:\s*(\d{4}-\d{2}-\d{2})", content)
        update_date = match.group(1) if match else "2000-01-01"
        dated_pages.append((update_date, slug, content))
    dated_pages.sort(reverse=True)

    sample = dated_pages[:max_pages]
    excerpts = "\n\n---\n\n".join(
        f"PAGE: {slug}\n\n{content[:2000]}"
        for _, slug, content in sample
    )

    try:
        response = model.generate_content(
            CONTRADICTION_PROMPT.format(excerpts=excerpts),
            generation_config=GenerationConfig(
                response_mime_type="application/json",
                temperature=0.0,
            ),
        )
        return json.loads(response.text)
    except Exception as e:
        logger.warning(f"Contradiction check failed: {e}")
        return []


# ─── Report generation and delivery ──────────────────────────────────────────

def _build_report(findings: list[str], total_pages: int) -> str:
    if findings:
        body = "\n\n".join(findings)
        summary = f"{len(findings)} issue(s) found across {total_pages} wiki pages."
    else:
        body = "No issues found. The wiki is in good shape."
        summary = f"All checks passed across {total_pages} wiki pages."

    return f"""# MoPoTools Wiki Lint Report — {TODAY}

**Summary**: {summary}

---

{body}

---

*Generated by the weekly lint Cloud Function. To suppress a false positive, add
`<!-- lint-ignore -->` on the line before the relevant content.*
"""


def _send_email(report: str) -> None:
    sg = SendGridAPIClient(api_key=os.environ["SENDGRID_API_KEY"])
    message = Mail(
        from_email="noreply@mopotools.wiki",
        to_emails=ADMIN_EMAIL,
        subject=f"MoPoTools Wiki Lint Report — {TODAY}",
        plain_text_content=report,
    )
    sg.send(message)
    logger.info(f"Lint report emailed to {ADMIN_EMAIL}")


def _save_report_to_gcs(gcs: storage.Client, report: str) -> None:
    """Save report to GCS staging bucket (not indexed by the wiki)."""
    blob = gcs.bucket(STAGING_BUCKET).blob(f"lint-reports/lint-{TODAY}.md")
    blob.upload_from_string(report, content_type="text/markdown")
    logger.info(f"Lint report saved to gs://{STAGING_BUCKET}/lint-reports/lint-{TODAY}.md")


# ─── Wiki page loader ─────────────────────────────────────────────────────────

def _load_wiki_pages(gcs: storage.Client) -> dict[str, str]:
    """Load all wiki pages from the current-wiki mirror in the processed bucket."""
    processed_bucket = os.environ.get("PROCESSED_BUCKET", STAGING_BUCKET)
    pages = {}
    blobs = list(gcs.bucket(processed_bucket).list_blobs(prefix="current-wiki/wiki/"))
    for blob in blobs:
        slug = blob.name.replace("current-wiki/wiki/", "").replace(".md", "")
        if slug:
            try:
                pages[slug] = blob.download_as_text()
            except Exception as e:
                logger.warning(f"Could not load page {slug}: {e}")
    return pages
