"""
Stage 4.4 — Sweden / Riksbank attribution validator.
Runs after all wiki pages are generated to catch geographic misattributions.
"""

import json
import logging
from typing import Any

import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig

from prompts import SWEDEN_CHECK_SYSTEM, SWEDEN_CHECK_USER

logger = logging.getLogger(__name__)

# Source file slugs known to be Swedish sources
SWEDISH_SOURCE_PATTERNS = [
    "riksbank",
    "jomaa-nora",
    "sse-thesis",
    "no-402",   # Riksbank working papers
    "no-404",
    "no-447",
    "riksbank-evaluation",
]


def run_sweden_check(
    slug: str,
    geographies: list[str],
    pages: dict[str, str],   # {page_slug: page_content}
    model: GenerativeModel,
) -> dict[str, Any]:
    """
    Run the Sweden attribution check on all generated pages.

    Returns:
        {
            "ok": bool,
            "violations": [ {"page_slug": ..., "claim": ..., "issue": ...} ]
        }
    """
    # Quick pre-check: if Sweden/Riksbank is not in the geographies list
    # and none of the generated pages mention Sweden, skip the full LLM check
    sweden_mentioned = any(
        "sweden" in g.lower() or "riksbank" in g.lower()
        for g in geographies
    )
    pages_mention_sweden = any(
        "sweden" in content.lower() or "riksbank" in content.lower()
        for content in pages.values()
    )

    if not sweden_mentioned and not pages_mention_sweden:
        logger.info(f"[{slug}] Sweden check: no Sweden/Riksbank content — skipping LLM call")
        return {"ok": True, "violations": []}

    logger.info(f"[{slug}] Sweden content detected — running full attribution check")

    pages_content = "\n\n---\n\n".join(
        f"PAGE: {page_slug}\n\n{content}"
        for page_slug, content in pages.items()
    )

    prompt = SWEDEN_CHECK_USER.format(
        slug=slug,
        geographies=", ".join(geographies),
        pages_content=pages_content[:80_000],  # truncate to stay within context
    )

    response = model.generate_content(
        [SWEDEN_CHECK_SYSTEM, prompt],
        generation_config=GenerationConfig(
            response_mime_type="application/json",
            temperature=0.0,
        ),
    )

    try:
        result = json.loads(response.text)
    except json.JSONDecodeError:
        logger.error(f"[{slug}] Sweden check returned invalid JSON: {response.text[:500]}")
        # Fail safe — treat as a violation requiring review
        return {
            "ok": False,
            "violations": [{
                "page_slug": "unknown",
                "claim": "Sweden check returned malformed JSON",
                "issue": "Manual review required",
            }],
        }

    violations = result.get("violations", [])
    if violations:
        logger.warning(
            f"[{slug}] Sweden check found {len(violations)} violation(s): "
            + json.dumps(violations, indent=2)
        )
    else:
        logger.info(f"[{slug}] Sweden check passed — no violations")

    return {"ok": len(violations) == 0, "violations": violations}


def source_is_swedish(slug: str) -> bool:
    """Return True if the source slug matches known Swedish sources."""
    slug_lower = slug.lower()
    return any(pattern in slug_lower for pattern in SWEDISH_SOURCE_PATTERNS)
