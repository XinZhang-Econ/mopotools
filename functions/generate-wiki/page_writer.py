"""
Page format validation and normalisation.
Ensures every generated page conforms to the CLAUDE.md page format before it
is written to the staging bucket.
"""

import re
from dataclasses import dataclass, field
from datetime import date


REQUIRED_FIELDS = [
    "Summary",
    "Research classification",
    "Sources",
    "Last updated",
]

VALID_CLASSIFICATIONS = {"empirical", "theoretical", "both"}

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$")


@dataclass
class ValidationResult:
    ok: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def validate_page(slug: str, content: str) -> ValidationResult:
    """
    Validate a generated wiki page against the CLAUDE.md format rules.
    Returns a ValidationResult describing any problems found.
    """
    errors = []
    warnings = []

    # 1. Slug format
    if not SLUG_RE.match(slug):
        errors.append(f"Slug '{slug}' must be lowercase-hyphen (e.g. 'my-page')")

    # 2. Must start with a # heading
    lines = content.splitlines()
    if not lines or not lines[0].startswith("# "):
        errors.append("Page must start with a # heading (page title)")

    # 3. Required header fields
    for field_name in REQUIRED_FIELDS:
        pattern = rf"\*\*{re.escape(field_name)}\*\*\s*:"
        if not re.search(pattern, content):
            errors.append(f"Missing required field: **{field_name}**")

    # 4. Research classification must be one of the valid values
    cls_match = re.search(r"\*\*Research classification\*\*\s*:\s*(.+)", content)
    if cls_match:
        cls_value = cls_match.group(1).strip().lower()
        if cls_value not in VALID_CLASSIFICATIONS:
            errors.append(
                f"**Research classification** must be one of: "
                f"{', '.join(VALID_CLASSIFICATIONS)} — got '{cls_value}'"
            )

    # 5. Last updated must be a valid date
    date_match = re.search(r"\*\*Last updated\*\*\s*:\s*(\d{4}-\d{2}-\d{2})", content)
    if date_match:
        try:
            date.fromisoformat(date_match.group(1))
        except ValueError:
            errors.append("**Last updated** must be in YYYY-MM-DD format")
    else:
        errors.append("**Last updated** field must contain a date in YYYY-MM-DD format")

    # 6. Must have a ## Related pages section
    if "## Related pages" not in content:
        errors.append("Page must include a '## Related pages' section")

    # 7. Warn on wiki-links that contain uppercase or spaces (likely formatting errors)
    wikilinks = re.findall(r"\[\[([^\]]+)\]\]", content)
    for link in wikilinks:
        if link != link.lower():
            warnings.append(f"Wiki-link [[{link}]] should be lowercase")
        if " " in link:
            warnings.append(f"Wiki-link [[{link}]] contains spaces — use hyphens")

    # 8. Warn on numeric values without obvious units
    # Look for bare numbers (integers or decimals) not followed by a unit
    bare_numbers = re.findall(
        r"(?<!\w)(\d+(?:\.\d+)?)(?!\s*(?:%|bp|bps|bn|billion|million|trillion|percent|pp|USD|GBP|EUR|SEK|JPY|of GDP|\w))",
        content,
    )
    if bare_numbers:
        warnings.append(
            f"Found {len(bare_numbers)} potentially bare numeric value(s) — "
            "ensure all numbers include units (currency or % of GDP)"
        )

    # 9. Warn on claims without source citations
    # Heuristic: sentences ending without (source: ...) in the main body
    body_match = re.search(r"---\n(.+)", content, re.DOTALL)
    if body_match:
        body = body_match.group(1)
        sentences = re.split(r"(?<=[.!?])\s+", body)
        uncited = [
            s for s in sentences
            if len(s) > 60
            and "(source:" not in s
            and not s.startswith(("#", "-", "*", ">", "[[", "**"))
        ]
        if uncited:
            warnings.append(
                f"{len(uncited)} long sentence(s) appear to lack (source: ...) citations"
            )

    return ValidationResult(ok=len(errors) == 0, errors=errors, warnings=warnings)


def normalise_slug(raw_name: str) -> str:
    """Convert a page title or filename to a valid wiki slug."""
    slug = raw_name.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    return slug


def extract_frontmatter(content: str) -> dict:
    """
    Parse the **Field**: value header lines from a wiki page.
    Returns a dict of field names to values.
    """
    result = {}
    for match in re.finditer(r"\*\*([^*]+)\*\*\s*:\s*(.+)", content):
        result[match.group(1).strip()] = match.group(2).strip()
    return result


def page_title(content: str) -> str | None:
    """Extract the # Title from a page."""
    match = re.match(r"#\s+(.+)", content)
    return match.group(1).strip() if match else None
