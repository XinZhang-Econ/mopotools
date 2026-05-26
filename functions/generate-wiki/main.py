"""
Stage 4 — AI Wiki Generation Cloud Function
Follows the CLAUDE.md ingest protocol exactly:
  1. Discussion pass (key takeaways)
  2. Summary page generation
  3. Concept page create/update
  4. index.md patch
  5. log.md entry
  6. Sweden attribution check
  7. Write all pages to staging bucket
"""

import json
import logging
import os
from datetime import date

import functions_framework
import vertexai
from google.cloud import firestore, storage
from vertexai.generative_models import GenerationConfig, GenerativeModel

from page_writer import normalise_slug, validate_page
from prompts import (
    CONCEPT_PAGE_CREATE_USER,
    CONCEPT_PAGE_SYSTEM,
    CONCEPT_PAGE_UPDATE_USER,
    DISCUSSION_SYSTEM,
    DISCUSSION_USER,
    INDEX_PATCH_SYSTEM,
    INDEX_PATCH_USER,
    LOG_ENTRY_TEMPLATE,
    SUMMARY_PAGE_SYSTEM,
    SUMMARY_PAGE_USER,
)
from sweden_check import run_sweden_check

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GCP_PROJECT      = os.environ["GCP_PROJECT"]
STAGING_BUCKET   = os.environ["STAGING_BUCKET"]
PROCESSED_BUCKET = os.environ["PROCESSED_BUCKET"]
WIKI_REPO        = os.environ["WIKI_REPO"]
TODAY            = date.today().isoformat()
MODEL_NAME       = "gemini-1.5-pro"
REGION           = "europe-west1"


@functions_framework.http
def generate_wiki(request):
    """
    Expected JSON body:
    {
        "slug": "bernanke-2020-new-tools",
        "tag":  "conventional-qe"
    }
    """
    body = request.get_json(force=True)
    slug = body["slug"]
    tag  = body["tag"]

    logger.info(f"[{slug}] Starting wiki generation (tag={tag})")

    db  = firestore.Client(project=GCP_PROJECT)
    gcs = storage.Client()

    vertexai.init(project=GCP_PROJECT, location=REGION)
    model = GenerativeModel(MODEL_NAME)

    try:
        # ── 1. Load extracted text ──────────────────────────────────────────
        processed_text = _load_processed_text(gcs, slug)

        # ── 2. Load existing wiki state (index.md + existing page list) ────
        existing_index, existing_pages = _load_existing_wiki(gcs, db)

        # ── 3. Discussion pass ─────────────────────────────────────────────
        logger.info(f"[{slug}] Running discussion pass")
        discussion = _run_discussion_pass(model, slug, tag, processed_text)
        logger.info(f"[{slug}] Discussion pass complete: {len(discussion['key_findings'])} findings")

        # ── 4. Generate summary page ───────────────────────────────────────
        logger.info(f"[{slug}] Generating summary page")
        summary_page = _generate_summary_page(model, slug, tag, discussion)
        _validate_or_raise(slug, summary_page)

        # ── 5. Generate / update concept pages ────────────────────────────
        logger.info(f"[{slug}] Processing {len(discussion['concept_pages_needed'])} concept pages")
        concept_pages = {}
        for concept in discussion["concept_pages_needed"]:
            concept_slug    = normalise_slug(concept["slug"])
            concept_title   = concept["title"]
            existing_content = existing_pages.get(concept_slug)

            if existing_content:
                logger.info(f"[{slug}] Updating existing concept page: {concept_slug}")
                page_content = _update_concept_page(
                    model, slug, concept_slug, existing_content, discussion
                )
            else:
                logger.info(f"[{slug}] Creating new concept page: {concept_slug}")
                page_content = _create_concept_page(
                    model, slug, concept_slug, concept_title,
                    discussion, list(existing_pages.keys())
                )

            _validate_or_raise(concept_slug, page_content)
            concept_pages[concept_slug] = page_content

        # ── 6. Patch index.md ──────────────────────────────────────────────
        logger.info(f"[{slug}] Patching index.md")
        new_index = _patch_index(model, existing_index, slug, concept_pages)

        # ── 7. Sweden check ────────────────────────────────────────────────
        logger.info(f"[{slug}] Running Sweden attribution check")
        all_pages = {slug: summary_page, **concept_pages}
        sweden_result = run_sweden_check(slug, discussion.get("geographies", []), all_pages, model)

        if not sweden_result["ok"]:
            db.collection("papers").document(slug).update({
                "status":            "sweden-check-failed",
                "swedenViolations":  sweden_result["violations"],
            })
            logger.error(f"[{slug}] Sweden check failed — halting pipeline")
            return {
                "status": "sweden-check-failed",
                "violations": sweden_result["violations"],
            }, 422

        # ── 8. Build log.md entry ──────────────────────────────────────────
        created_pages = [p for p in concept_pages if p not in existing_pages]
        updated_pages = [p for p in concept_pages if p in existing_pages]
        log_entry = LOG_ENTRY_TEMPLATE.format(
            today=TODAY,
            slug=slug,
            created_pages=", ".join([f"wiki/{slug}.md"] + [f"wiki/{p}.md" for p in created_pages]) or "none",
            updated_pages=", ".join(f"wiki/{p}.md" for p in updated_pages) or "none",
            new_index_entries=len(concept_pages) + 1,
            plural="y" if (len(concept_pages) + 1) == 1 else "ies",
        )

        # ── 9. Write all pages to staging bucket ───────────────────────────
        logger.info(f"[{slug}] Writing {1 + len(concept_pages)} pages to staging")
        staging = gcs.bucket(STAGING_BUCKET)

        staging.blob(f"{slug}/wiki/{slug}.md").upload_from_string(
            summary_page, content_type="text/markdown"
        )
        for page_slug, content in concept_pages.items():
            staging.blob(f"{slug}/wiki/{page_slug}.md").upload_from_string(
                content, content_type="text/markdown"
            )
        staging.blob(f"{slug}/wiki/index.md").upload_from_string(
            new_index, content_type="text/markdown"
        )
        staging.blob(f"{slug}/log_entry.md").upload_from_string(
            log_entry, content_type="text/markdown"
        )
        staging.blob(f"{slug}/discussion.json").upload_from_string(
            json.dumps(discussion, indent=2), content_type="application/json"
        )
        staging.blob(f"{slug}/sweden_check.json").upload_from_string(
            json.dumps(sweden_result, indent=2), content_type="application/json"
        )

        # ── 10. Update Firestore status ────────────────────────────────────
        db.collection("papers").document(slug).update({
            "status":          "awaiting-review",
            "pagesGenerated":  list(all_pages.keys()),
            "conceptsCreated": created_pages,
            "conceptsUpdated": updated_pages,
            "swedenCheck":     "passed",
        })

        logger.info(f"[{slug}] Wiki generation complete — awaiting moderator review")
        return {
            "status":   "awaiting-review",
            "slug":     slug,
            "pages":    list(all_pages.keys()),
            "staging":  f"gs://{STAGING_BUCKET}/{slug}/",
        }, 200

    except Exception as exc:
        logger.exception(f"[{slug}] Wiki generation failed: {exc}")
        db.collection("papers").document(slug).update({"status": "generation-failed", "error": str(exc)})
        return {"status": "error", "message": str(exc)}, 500


# ─── Helper functions ─────────────────────────────────────────────────────────

def _load_processed_text(gcs: storage.Client, slug: str) -> str:
    blob = gcs.bucket(PROCESSED_BUCKET).blob(f"{slug}.md")
    return blob.download_as_text()


def _load_existing_wiki(gcs: storage.Client, db: firestore.Client) -> tuple[str, dict[str, str]]:
    """
    Load the current wiki state from the Git repository via the staging bucket's
    reference copy, or fall back to Firestore-tracked page list.
    Returns (index_content, {page_slug: page_content}).
    """
    staging = gcs.bucket(PROCESSED_BUCKET)

    # Try to load current index.md
    index_blob = staging.blob("current-wiki/index.md")
    try:
        index_content = index_blob.download_as_text()
    except Exception:
        index_content = "# Monetary Policy Tools Wiki\n\n**Last updated**: " + TODAY + "\n\n---\n\n"

    # Load all existing wiki pages (stored in processed/ as current-wiki/<slug>.md)
    existing_pages = {}
    blobs = list(gcs.bucket(PROCESSED_BUCKET).list_blobs(prefix="current-wiki/wiki/"))
    for blob in blobs:
        page_slug = blob.name.replace("current-wiki/wiki/", "").replace(".md", "")
        if page_slug and page_slug != "index" and page_slug != "log":
            try:
                existing_pages[page_slug] = blob.download_as_text()
            except Exception:
                pass

    return index_content, existing_pages


def _run_discussion_pass(model: GenerativeModel, slug: str, tag: str, text: str) -> dict:
    """Pass 1: extract key takeaways as structured JSON."""
    prompt = DISCUSSION_USER.format(slug=slug, tag=tag, text=text[:200_000])
    response = model.generate_content(
        [DISCUSSION_SYSTEM, prompt],
        generation_config=GenerationConfig(
            response_mime_type="application/json",
            temperature=0.1,
            max_output_tokens=4096,
        ),
    )
    return json.loads(response.text)


def _generate_summary_page(model: GenerativeModel, slug: str, tag: str, discussion: dict) -> str:
    """Pass 2a: generate the summary page for this source."""
    system = SUMMARY_PAGE_SYSTEM.format(slug=slug, today=TODAY)
    prompt = SUMMARY_PAGE_USER.format(
        slug=slug,
        tag=tag,
        today=TODAY,
        discussion_json=json.dumps(discussion, indent=2),
    )
    response = model.generate_content(
        [system, prompt],
        generation_config=GenerationConfig(temperature=0.2, max_output_tokens=8192),
    )
    return response.text.strip()


def _create_concept_page(
    model: GenerativeModel,
    slug: str,
    concept_slug: str,
    concept_title: str,
    discussion: dict,
    existing_page_list: list[str],
) -> str:
    """Pass 2b: create a brand-new concept page."""
    system = CONCEPT_PAGE_SYSTEM.format(today=TODAY)
    # Pull relevant excerpts from the discussion pass
    relevant = _excerpts_for_concept(concept_slug, discussion)
    prompt = CONCEPT_PAGE_CREATE_USER.format(
        concept_slug=concept_slug,
        concept_title=concept_title,
        slug=slug,
        relevant_excerpts=relevant,
        existing_page_list="\n".join(f"- [[{p}]]" for p in existing_page_list),
        today=TODAY,
    )
    response = model.generate_content(
        [system, prompt],
        generation_config=GenerationConfig(temperature=0.2, max_output_tokens=6144),
    )
    return response.text.strip()


def _update_concept_page(
    model: GenerativeModel,
    slug: str,
    concept_slug: str,
    existing_content: str,
    discussion: dict,
) -> str:
    """Pass 2b: update an existing concept page with new information."""
    system = CONCEPT_PAGE_SYSTEM.format(today=TODAY)
    relevant = _excerpts_for_concept(concept_slug, discussion)
    prompt = CONCEPT_PAGE_UPDATE_USER.format(
        concept_slug=concept_slug,
        slug=slug,
        existing_content=existing_content,
        relevant_excerpts=relevant,
        today=TODAY,
    )
    response = model.generate_content(
        [system, prompt],
        generation_config=GenerationConfig(temperature=0.2, max_output_tokens=8192),
    )
    return response.text.strip()


def _patch_index(
    model: GenerativeModel,
    current_index: str,
    slug: str,
    new_pages: dict[str, str],
) -> str:
    """Pass 2c: patch index.md with new entries."""
    new_pages_info = [
        {"slug": s, "title": s.replace("-", " ").title(), "description": "See page for details.", "section": "Other"}
        for s in [slug] + list(new_pages.keys())
    ]
    system = INDEX_PATCH_SYSTEM.format(today=TODAY)
    prompt = INDEX_PATCH_USER.format(
        current_index=current_index,
        new_pages_json=json.dumps(new_pages_info, indent=2),
        today=TODAY,
    )
    response = model.generate_content(
        [system, prompt],
        generation_config=GenerationConfig(temperature=0.1, max_output_tokens=4096),
    )
    return response.text.strip()


def _excerpts_for_concept(concept_slug: str, discussion: dict) -> str:
    """Extract relevant passages from the discussion JSON for a specific concept."""
    relevant_lines = []
    concept_keywords = concept_slug.replace("-", " ").split()

    for finding in discussion.get("key_findings", []):
        if any(kw in finding.lower() for kw in concept_keywords):
            relevant_lines.append(f"- {finding}")

    for claim in discussion.get("numeric_claims", []):
        if any(kw in claim["claim"].lower() for kw in concept_keywords):
            relevant_lines.append(
                f"- {claim['claim']} [{claim['value']} — {claim['geography']}]"
                f" (source: {claim['source_section']})"
            )

    if not relevant_lines:
        # Fallback: return the main argument + all findings
        relevant_lines = [f"Main argument: {discussion.get('main_argument', '')}"]
        relevant_lines += [f"- {f}" for f in discussion.get("key_findings", [])]

    return "\n".join(relevant_lines)


def _validate_or_raise(slug: str, content: str) -> None:
    """Validate a page and raise ValueError if it has format errors."""
    from page_writer import validate_page
    result = validate_page(slug, content)
    if not result.ok:
        raise ValueError(
            f"Page '{slug}' failed format validation:\n" + "\n".join(result.errors)
        )
    if result.warnings:
        logger.warning(f"[{slug}] Page warnings: " + "; ".join(result.warnings))
