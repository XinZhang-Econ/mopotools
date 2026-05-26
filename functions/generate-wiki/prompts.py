"""
Prompt templates for Stage 4 — AI Wiki Generation.
All prompts are designed to enforce the CLAUDE.md protocol exactly.
"""

from datetime import date


# ─── Pass 1: Discussion / key-takeaway extraction ─────────────────────────────

DISCUSSION_SYSTEM = """You are a research assistant specialising in monetary policy economics.
Your task is to read an academic paper and extract structured key takeaways.
Be precise about geographic scope — never mix data from different countries.
Pay special attention to Sweden/Riksbank data and ensure it is labelled correctly.
Return ONLY valid JSON matching the schema provided."""

DISCUSSION_USER = """Read the following paper and extract key information.

Paper slug: {slug}
Policy tag: {tag}

--- PAPER TEXT ---
{text}
--- END PAPER ---

Return a JSON object with exactly these fields:
{{
  "title": "Full paper title",
  "authors": ["Last, First", ...],
  "year": 2024,
  "main_argument": "One sentence summary of the central claim",
  "key_findings": ["Finding 1 with numeric values where present", ...],
  "policy_instruments": ["List of monetary policy instruments discussed"],
  "geographies": ["Countries or regions explicitly studied"],
  "methodology": "Brief description of empirical/theoretical method",
  "numeric_claims": [
    {{
      "claim": "Exact claim text",
      "value": "Numeric value with units (e.g. 100bp or 2.5% of GDP)",
      "geography": "Country or region this applies to",
      "source_section": "e.g. Section 3 or Table 2"
    }}
  ],
  "contradicts_slugs": ["slug of any paper in the existing wiki this contradicts"],
  "related_wiki_pages": ["existing wiki page slugs this paper is relevant to"],
  "concept_pages_needed": [
    {{
      "slug": "lowercase-hyphen-slug",
      "title": "Page Title",
      "is_new": true
    }}
  ],
  "sweden_claims": [
    {{
      "claim": "Any claim about Sweden/Riksbank",
      "source_section": "Where in the paper",
      "source_confirmed": true
    }}
  ]
}}"""


# ─── Pass 2a: Summary page generation ────────────────────────────────────────

SUMMARY_PAGE_SYSTEM = """You are maintaining an academic wiki on monetary policy.
You write wiki pages in strict Markdown following a defined format.
Every factual claim must end with (source: {slug}.pdf).
Every numeric value must include its unit (currency amount or % of GDP) — never a bare number.
Write in clear, plain language. Use [[wiki-links]] to link to related concept pages.
Today's date is {today}."""

SUMMARY_PAGE_USER = """Write a wiki summary page for this paper.

Slug: {slug}
Policy tag: {tag}

Key takeaways from the discussion pass:
{discussion_json}

The page MUST follow this exact format:

# {{Title}}

**Summary**: {{1–3 sentences}}

**Research classification**: {{empirical | theoretical | both}}

**Sources**: {slug}.pdf

**Last updated**: {today}

---

## Abstract

{{Faithful summary of the abstract}}

## Key Findings

{{Each major finding as a paragraph with (source: {slug}.pdf) after every factual claim.
All numeric values include units.}}

## Methodology

{{Description of empirical or theoretical method}}

## Policy Implications

{{What this paper implies for central bank practice}}

## Contradictions and Debates

{{If this paper contradicts another source in the wiki, note it explicitly with both sources.
Leave this section empty (write "None identified.") if there are no contradictions.}}

## Related pages

{{A bulleted list of [[wiki-links]] to related concept pages}}

Do not add any text before the # heading or after the Related pages section."""


# ─── Pass 2b: Concept page update ─────────────────────────────────────────────

CONCEPT_PAGE_SYSTEM = """You are maintaining an academic wiki on monetary policy.
You are updating or creating a concept page.
Every factual claim must end with (source: filename.pdf).
Every numeric value must include its unit — never a bare number.
Write in clear, plain language. Use [[wiki-links]] to link to related pages.
Today's date is {today}."""

CONCEPT_PAGE_CREATE_USER = """Create a new wiki concept page.

Page slug: {concept_slug}
Page title: {concept_title}
New information from paper "{slug}.pdf":
{relevant_excerpts}

Existing wiki pages for context (do not duplicate their content, just link to them):
{existing_page_list}

The page MUST follow this exact format:

# {{Title}}

**Summary**: {{1–3 sentences}}

**Research classification**: {{empirical | theoretical | both}}

**Sources**: {slug}.pdf

**Last updated**: {today}

---

{{Main content. Use ##-level headings for sub-topics.
After every factual claim: (source: filename.pdf).
All numeric values include units.
Link to related pages with [[wiki-links]].}}

## Related pages

- [[related-1]]
- [[related-2]]"""


CONCEPT_PAGE_UPDATE_USER = """Update an existing wiki concept page with new information from a paper.

Page slug: {concept_slug}
New source: {slug}.pdf

--- EXISTING PAGE ---
{existing_content}
--- END EXISTING PAGE ---

New information to integrate:
{relevant_excerpts}

Rules:
- Add new information without removing existing content
- If the new source contradicts existing claims, note the contradiction explicitly
- Update **Sources** to include {slug}.pdf if not already listed
- Update **Last updated** to {today}
- Keep all existing [[wiki-links]]
- Add new [[wiki-links]] where relevant
- Every new factual claim: (source: {slug}.pdf)
- Every numeric value includes units

Return the complete updated page."""


# ─── Pass 2c: index.md patch ─────────────────────────────────────────────────

INDEX_PATCH_SYSTEM = """You are updating a wiki table of contents (index.md).
You add new page entries without removing or reordering existing ones.
Today's date is {today}."""

INDEX_PATCH_USER = """Update this wiki index.md to include new pages.

--- CURRENT INDEX ---
{current_index}
--- END INDEX ---

New pages to add:
{new_pages_json}

Each entry in new_pages_json has: slug, title, description, section.

Rules:
- Insert each new page under its appropriate section heading
- Format: - [[slug]] - One-line description
- If the section doesn't exist, add it at the end before "## Related Pages"
- Update **Last updated** to {today}
- Do not remove or reorder existing entries

Return the complete updated index.md."""


# ─── Pass 2d: log.md entry ────────────────────────────────────────────────────

LOG_ENTRY_TEMPLATE = """
## {today} — {slug}.pdf

- Created: {created_pages}
- Updated: {updated_pages}
- index.md: added {new_index_entries} entr{plural}
"""


# ─── Sweden validation prompt ─────────────────────────────────────────────────

SWEDEN_CHECK_SYSTEM = """You are a careful fact-checker for an academic wiki.
Your task is to review wiki pages for geographic attribution errors.
Pay special attention to claims about Sweden, the Riksbank, and Swedish monetary policy."""

SWEDEN_CHECK_USER = """Review the following generated wiki pages for geographic attribution errors.

Source paper: {slug}.pdf
Geographies in paper: {geographies}

--- GENERATED PAGES ---
{pages_content}
--- END GENERATED PAGES ---

Check for any claim about Sweden, the Riksbank, or Swedish monetary policy.
For each such claim:
1. Confirm it cites a Swedish source (file slug contains: riksbank, jomaa-nora, sse-thesis, or similar)
2. Confirm it is NOT attributed to ECB, Bank of England, Federal Reserve, or other non-Swedish institutions
3. Confirm it is NOT a Sweden claim that should actually apply to another country

Return JSON:
{{
  "violations": [
    {{
      "page_slug": "wiki page where the violation occurs",
      "claim": "The problematic claim text",
      "issue": "Description of the attribution error"
    }}
  ],
  "ok": true  // true if violations is empty
}}"""
