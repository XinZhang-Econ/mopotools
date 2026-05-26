# MoPoTools — GCP Ingest Pipeline

**Summary**: End-to-end architecture for ingesting research papers, generating wiki pages following the CLAUDE.md protocol, and serving the knowledge base on Google Cloud Platform.

**Last updated**: 2026-05-26

---

## Overview

This document describes the full pipeline for the MoPoTools wiki platform. Contributors upload papers through a web interface; an automated pipeline extracts text, generates wiki pages following the rules in `CLAUDE.md`, and publishes them to the Quartz-based wiki site. The pipeline runs entirely on GCP.

```
Contributor browser
  └─ Upload form (Cloud Run / Next.js)
       └─ PDF → Cloud Storage  raw/<slug>.md   [immutable]
            └─ Cloud Workflows trigger
                 ├─ Stage 3: Text extraction    (Document AI)
                 ├─ Stage 4: AI wiki generation (Vertex AI Gemini)
                 │     ├─ wiki/<source>.md      (summary page)
                 │     ├─ wiki/<concept-N>.md   (create / update)
                 │     ├─ wiki/index.md         (patched)
                 │     └─ wiki/log.md           (appended)
                 └─ Stage 5: Moderator review   (Cloud Run UI)
                      └─ Approved → git commit → Cloud Build
                           └─ Quartz rebuild → Cloud Run (wiki site)
```

---

## Folder Conventions

The local folder layout is preserved exactly in Cloud Storage and in the Git repository:

| Path | Purpose | Mutability |
|------|---------|------------|
| `raw/` | Uploaded source documents | **Immutable** — object lock enforced |
| `wiki/` | Markdown pages maintained by pipeline + human | Writable by pipeline and admins |
| `wiki/index.md` | Table of contents — updated on every ingest | Always updated |
| `wiki/log.md` | Append-only operation record | Append only — never overwritten |

---

## Stage 1 — Access & Authentication

**GCP services**: Identity-Aware Proxy (IAP), Google Identity Platform, Firestore

All traffic to the upload frontend and moderator UI passes through IAP. Users authenticate via Google SSO. A Firestore document at `users/{uid}` carries a `role` field:

- `admin` — full access; can approve/reject ingestions and manage users
- `contributor` — can upload papers and view their own submission status
- `reader` — read-only access to the published wiki site

Only contributors and admins may upload. The wiki site itself may be public or IAP-gated depending on preference.

---

## Stage 2 — Upload & Tagging

**GCP services**: Cloud Storage, Firestore, Cloud Run (frontend)

### Upload flow

1. Contributor fills in the upload form: title, authors, year, policy tag, and file.
2. The backend issues a **signed upload URL** for `gs://mopotools-raw/<slug>.<ext>`.
3. The browser uploads directly to Cloud Storage — no file bytes transit the app server.
4. On upload completion, a Firestore document is created at `papers/{slug}`:

```json
{
  "slug": "bernanke-2020-new-tools",
  "title": "New Tools for Policy when the Short Rate is at Zero",
  "authors": ["Bernanke, B.S."],
  "year": 2020,
  "tag": "conventional-qe",
  "rawPath": "gs://mopotools-raw/bernanke-2020-new-tools.pdf",
  "uploader": "uid-abc123",
  "status": "pending",
  "uploadedAt": "2026-05-26T10:00:00Z"
}
```

### Policy tags (controlled vocabulary)

| Tag value | Display label |
|-----------|---------------|
| `conventional` | Conventional monetary policy |
| `conventional-qe` | Conventional — Quantitative Easing |
| `unconventional` | Unconventional monetary policy |
| `forward-guidance` | Forward Guidance |
| `negative-rates` | Negative Interest Rates |
| `yield-curve-control` | Yield Curve Control |

### Immutability

Cloud Storage bucket `mopotools-raw` is configured with:
- **Object versioning** enabled
- **Retention policy**: 3650 days (10 years)
- IAM: no `storage.objects.delete` permission for any service account used by the pipeline

---

## Stage 3 — Text Extraction

**GCP services**: Cloud Workflows, Document AI, Cloud Storage

A Cloud Storage `finalize` Pub/Sub event triggers a Cloud Workflows execution. The workflow calls a Cloud Function `extract-text`:

1. Calls Document AI (Form Parser / OCR processor) on the uploaded file.
2. Produces a clean Markdown representation of the full text.
3. For **large documents** (>50 pages), splits output into labelled sections: `abstract`, `introduction`, `body`, `conclusion`, `references`.
4. Saves the extracted text to `gs://mopotools-processed/<slug>.md`.
5. Updates Firestore `papers/{slug}.status = "extracted"`.

**OCR fallback**: If Document AI detects a scanned page (no embedded text), it automatically applies OCR before returning content.

---

## Stage 4 — AI Wiki Generation (CLAUDE.md Protocol)

**GCP services**: Vertex AI Gemini, Cloud Functions, Cloud Storage, Firestore

This is the core stage. A Cloud Function `generate-wiki` is called by the workflow after successful text extraction. It strictly follows the ingest rules in `CLAUDE.md`.

### 4.1 Discussion pass (key takeaways)

Before writing any page, the model performs a structured extraction pass over the full text, producing a JSON summary:

```json
{
  "main_argument": "...",
  "key_findings": ["...", "..."],
  "policy_instruments": ["QE", "LSAP"],
  "geographies": ["United States", "Euro Area"],
  "methodology": "DSGE + event study",
  "numeric_claims": [
    {"claim": "QE reduced 10y yields by 100bp", "value": "100bp", "source_section": "Section 3"}
  ],
  "contradicts": ["fifty-shades-of-qe-pdf.md"],
  "related_wiki_pages": ["quantitative-easing", "effects-on-yields", "qe-united-states"]
}
```

### 4.2 Page writing pass

Using the discussion-pass JSON, the model writes or updates the following pages:

**A. Summary page** (`wiki/<slug>.md`)
Named after the source file. Follows the required page format exactly:

```markdown
# <Title>

**Summary**: <1–3 sentences>

**Research classification**: empirical | theoretical | both

**Sources**: <slug>.pdf

**Last updated**: YYYY-MM-DD

---

<Main content with citations and [[wiki-links]]>

## Related pages

- [[related-concept-1]]
- [[related-concept-2]]
```

**B. Concept pages** (`wiki/<concept>.md`)
For each major idea or entity identified in the discussion pass, the model creates a new page or appends a new section to an existing one. A single paper typically touches 10–15 pages.

**C. `wiki/index.md` patch**
New page entries are inserted under the appropriate section heading with one-line descriptions. Existing entries are never deleted.

**D. `wiki/log.md` append**
A single entry is appended (never overwritten):

```
## 2026-05-26 — bernanke-2020-new-tools.pdf
- Created: wiki/bernanke-2020-new-tools.md
- Updated: wiki/quantitative-easing.md, wiki/effects-on-yields.md, wiki/qe-united-states.md
- index.md: added 1 entry
```

### 4.3 Citation enforcement

Every factual claim in every generated page must:
- End with `(source: <filename>.pdf)` or `(source: <filename>.md)`
- Include explicit units for all numeric values — either a currency amount (e.g., "£375 billion") or a fraction of GDP (e.g., "~10% of GDP") — never a bare number
- If two sources disagree, note the contradiction explicitly with both source references
- If a claim has no source, append `(source: needs verification)`

### 4.4 Sweden check (mandatory validation step)

After page generation, a separate validation prompt runs:

> "Review all generated pages. Identify any claim that refers to Sweden, the Riksbank, or Swedish monetary policy. For each such claim, confirm it cites a Swedish source (riksbank-*, jomaa-nora-*, sse-thesis-*) and is not mixed with ECB, Bank of England, or Federal Reserve data. Return any violations as a JSON list."

If violations are found, the pipeline sets `papers/{slug}.status = "sweden-check-failed"` and halts. The admin is notified by email.

### 4.5 Output staging

All generated pages are written to `gs://mopotools-staging/<slug>/` — not directly to the live `wiki/` directory. The moderator review step (Stage 5) moves them.

Firestore update: `papers/{slug}.status = "awaiting-review"`

---

## Stage 5 — Moderator Review

**GCP services**: Cloud Run (moderator UI), Firestore, Cloud Build, GitHub

### Review UI

The moderator dashboard shows:
- A diff view of each new/changed wiki page (generated vs. current)
- Citation completeness indicator (% of claims with sources)
- Wiki-link validation: lists any `[[link]]` targets that do not resolve to an existing page
- The Sweden-check result
- The log.md entry to be appended

### Approval flow

On **Approve**:
1. Files are copied from `gs://mopotools-staging/<slug>/` to the Git repository `wiki/` directory via the Cloud Build service account.
2. A commit is created: `ingest: <slug> [auto]`
3. Cloud Build trigger fires (see Stage 6).
4. Firestore: `papers/{slug}.status = "published"`

On **Edit**: moderator edits pages inline, then approves.

On **Reject**: staging files are deleted. Firestore: `papers/{slug}.status = "rejected"`. Optional rejection note stored.

---

## Stage 6 — Display (Quartz on Cloud Run)

**GCP services**: Cloud Run, Cloud CDN, Cloud Build, GitHub

### Build trigger

A Cloud Build trigger watches the `main` branch of the wiki Git repository. On each new commit to `wiki/`:

```yaml
# cloudbuild.yaml
steps:
  - name: 'node:20'
    entrypoint: npm
    args: ['install']
    dir: 'quartz'
  - name: 'node:20'
    entrypoint: npx
    args: ['quartz', 'build']
    dir: 'quartz'
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/mopotools-wiki', '.']
  - name: 'gcr.io/cloud-builders/gcloud'
    args: ['run', 'deploy', 'mopotools-wiki',
           '--image', 'gcr.io/$PROJECT_ID/mopotools-wiki',
           '--region', 'europe-west1',
           '--platform', 'managed']
```

### Site structure

The Quartz site automatically organises pages by [[wiki-link]] graph. Policy tag subsections are generated from a `quartz.config.ts` explorer plugin that groups pages by the `tag` frontmatter field added during Stage 4.

### Search

Quartz full-text search covers all wiki pages. Vertex AI Search provides an additional semantic search endpoint called from the wiki site's search bar via a Cloud Run API proxy.

---

## Scheduled Lint Job

**GCP services**: Cloud Scheduler, Cloud Functions, SendGrid (email)

A Cloud Scheduler job fires every Monday at 08:00 UTC, triggering a Cloud Function `run-lint`. The function runs the full CLAUDE.md lint checklist against the current `wiki/` directory:

1. **Contradictions** — pairs of pages that make incompatible numeric claims about the same instrument/country
2. **Orphan pages** — pages with no inbound `[[wiki-link]]` from any other page
3. **Missing concept pages** — `[[wiki-links]]` that appear in text but have no corresponding `.md` file
4. **Outdated claims** — claims citing sources older than 5 years where a newer source on the same topic exists
5. **Format violations** — pages missing any required header field (`Summary`, `Research classification`, `Sources`, `Last updated`)

Output is a numbered Markdown report emailed to the admin and written to `wiki/lint-report-<YYYY-MM-DD>.md` (not indexed, for reference only).

---

## Repository & Project Structure

```
mopotools/
├── infra/                  # Terraform
│   ├── main.tf
│   ├── storage.tf
│   ├── firestore.tf
│   ├── cloud_run.tf
│   ├── workflows.tf
│   ├── scheduler.tf
│   └── iam.tf
├── functions/
│   ├── extract-text/       # Stage 3 Cloud Function
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── generate-wiki/      # Stage 4 Cloud Function
│   │   ├── main.py
│   │   ├── prompts.py      # All Gemini prompt templates
│   │   ├── page_writer.py  # Page format enforcement
│   │   ├── sweden_check.py # Stage 4.4 validation
│   │   └── requirements.txt
│   └── run-lint/           # Scheduled lint job
│       ├── main.py
│       └── requirements.txt
├── workflows/
│   └── ingest.yaml         # Cloud Workflows definition
├── frontend/               # Next.js upload + moderator UI
│   ├── app/
│   │   ├── upload/
│   │   └── review/
│   └── Dockerfile
├── wiki-site/              # Quartz configuration
│   ├── quartz.config.ts
│   ├── Dockerfile
│   └── cloudbuild.yaml
└── PIPELINE.md             # This file
```

---

## Environment Variables & Secrets

All secrets are stored in Secret Manager under the project. Cloud Functions and Cloud Run services are granted `secretmanager.secretAccessor` on their specific secrets only.

| Secret name | Used by | Description |
|-------------|---------|-------------|
| `vertex-ai-api-key` | `generate-wiki` | Vertex AI Gemini API key |
| `document-ai-processor-id` | `extract-text` | Document AI processor resource ID |
| `github-token` | Moderator approval flow | Token to commit to wiki repo |
| `sendgrid-api-key` | `run-lint` | Email delivery for lint reports |
| `iap-client-secret` | Cloud Run services | IAP OAuth client secret |

---

## Key Design Decisions

**Why Vertex AI Gemini for Stage 4?** Gemini 1.5 Pro's 1M-token context window allows the full text of even the longest papers to be processed in a single call, avoiding the complexity of chunked multi-call assembly when generating concept pages that span the whole document.

**Why Cloud Workflows rather than Cloud Functions chaining?** Cloud Workflows provides native retry logic, step-level error handling, and a visual execution graph in the GCP console. This makes debugging failed ingestions much easier than tracing chained Pub/Sub messages.

**Why Quartz rather than a custom wiki renderer?** Quartz already handles `[[wiki-link]]` resolution, graph view, backlinks, and full-text search — the exact features the wiki needs. Building these from scratch would be significant scope with no research value.

**Why a mandatory moderator review step?** The CLAUDE.md protocol requires discussing key takeaways before writing. The human moderator step is the lightweight equivalent: a trained researcher reviews the AI's output before it goes live, catching hallucinations and misattributions (especially the Sweden-mixing risk).
