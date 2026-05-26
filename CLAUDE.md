# LLM Wiki

A personal knowledge base maintained by Claude Code.
Based on Andrej Karpathy's LLM Wiki pattern. Extended by XZ to explore the use of LLM to construct central bank monetary policy tools (MoPoTools).

## Purpose

This wiki is a structured, interlinked knowledge base for understanding different unconventional monetary policy effects.
Claude maintains the wiki. The human curates sources, asks questions, and guides the analysis.

## Folder structure

```
raw/          -- source documents (immutable -- never modify these)
wiki/         -- markdown pages maintained by Claude
wiki/index.md -- table of contents for the entire wiki
wiki/log.md   -- append-only record of all operations
```

## Ingest workflow

When the user adds a new source to `raw/` and asks you to ingest it:

1. Read the full source document
2. If the full source document is too large, ingest each section separately with knowledge that these sections are connected to each other
3. Discuss key takeaways with the user before writing anything
4. Create a summary page in `wiki/` named after the source
5. Create or update concept pages for each major idea or entity
6. Add wiki-links ([[page-name]]) to connect related pages
7. Update `wiki/index.md` with new pages and one-line descriptions
8. Append an entry to `wiki/log.md` with the date, source name, and what changed
9. Make sure the source and information about Sweden is correctly specified and ingested. It would be embarrassing to mixed the information from other countries.

A single source may touch 10-15 wiki pages. That is normal.

## Page format

Every wiki page should follow this structure:

```markdown
# Page Title

**Summary**: One to three sentences describing this page.

**Research classification**: One of the following classification based on the type of research: empirical, theoretical, or both.

**Sources**: List of raw source files this page draws from.

**Last updated**: Date of most recent update.

---

Main content goes here. Use clear headings and short paragraphs.

Link to related concepts using [[wiki-links]] throughout the text.

## Related pages

- [[related-concept-1]]
- [[related-concept-2]]
```

## Citation rules

- Every factual claim should reference its source file
- Every factual claim with numeric values should reference its source file and write clearly about the measurement metrics, whether in currency amount or as fraction of the GDP
- Use the format (source: filename.pdf) after the claim
- If two sources disagree, note the contradiction explicitly
- If a claim has no source, mark it as needing verification

## Question answering

When the user asks a question:

1. Read `wiki/index.md` first to find relevant pages
2. Read those pages and synthesize an answer
3. Cite specific wiki pages in your response
4. If the answer is not in the wiki, say so clearly
5. If the answer is valuable, offer to save it as a new wiki page

Good answers should be filed back into the wiki so they compound over time.

## Lint

When the user asks you to lint or audit the wiki:

- Check for contradictions between pages
- Find orphan pages (no inbound links from other pages)
- Identify concepts mentioned in pages that lack their own page
- Flag claims that may be outdated based on newer sources
- Check that all pages follow the page format above
- Report findings as a numbered list with suggested fixes

## Rules

- Never modify anything in the `raw/` folder
- Always update `wiki/index.md` and `wiki/log.md` after changes
- Keep page names lowercase with hyphens (e.g. `machine-learning.md`)
- Write in clear, plain language
- When uncertain about how to categorize something, ask the user
