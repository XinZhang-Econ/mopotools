# Deploying MoPoTools to Google Cloud

This guide walks you through hosting the full MoPoTools pipeline on GCP: the wiki site, upload/review frontend, ingest Cloud Functions, and the weekly lint job.

**Estimated time**: 30–45 minutes for a first deployment.

---

## Prerequisites

Install these on your local machine before running `deploy.sh`:

| Tool | Version | Install |
|------|---------|---------|
| gcloud CLI | Latest | https://cloud.google.com/sdk/docs/install |
| Terraform | >= 1.6 | https://developer.hashicorp.com/terraform/install |
| Docker | Latest | https://docs.docker.com/get-docker/ |
| Git | Any | https://git-scm.com/ |
| Node.js | >= 18 | https://nodejs.org/ |

After installing gcloud, authenticate:

```bash
gcloud auth login
gcloud auth application-default login
```

---

## Step 1 — Create a GitHub repository

1. Go to https://github.com/new
2. Name it `mopotools` (or whatever you like — you'll enter it during deployment)
3. Set it to **Private**
4. Do **not** initialise with a README, .gitignore, or licence
5. Click **Create repository**

You'll also need a GitHub Personal Access Token with write access to this repo:

1. Go to https://github.com/settings/tokens?type=beta (Fine-grained tokens)
2. Click **Generate new token**
3. Set expiry to 1 year
4. Under **Repository access** → select your `mopotools` repo only
5. Under **Permissions** → Contents: **Read and write**, Metadata: **Read**
6. Copy the token — you'll enter it when `deploy.sh` asks for `github-token`

---

## Step 2 — Create a Document AI processor

The text extraction function needs a Document AI processor. This is a one-time setup:

1. Go to https://console.cloud.google.com/ai/document-ai
2. Select your GCP project (or create it first in Step 3)
3. Click **Create Processor**
4. Choose **Document OCR** (under "General")
5. Set region to match your deployment region (default: `europe-west1`)
6. Click **Create**
7. Copy the **Processor ID** from the processor detail page (a hex string like `abc1234567890`)

---

## Step 3 — Run the deployment script

```bash
cd /path/to/MoPoTools
chmod +x deploy.sh
./deploy.sh
```

The script will:

1. Check all prerequisites are installed
2. Ask you for: GitHub username, repo name, GCP region, admin email
3. Create the GCP project (or use an existing one)
4. Pause to let you link billing — **this is required before anything else works**
5. Create a Terraform state bucket
6. Run `terraform init` + `terraform plan` + `terraform apply`
7. Ask you to create the GitHub repo if you haven't already, then push the code
8. Ask for your Document AI processor ID
9. Prompt for each secret value (Vertex AI key, GitHub token, SendGrid key)
10. Build and push the frontend and wiki site Docker images via Cloud Build
11. Deploy the three Cloud Functions
12. Configure the Cloud Workflows ingest pipeline
13. Set up the Cloud Build trigger for wiki auto-rebuild
14. Print your live URLs

### What the script does NOT do automatically

These steps require manual action and are clearly called out during the script:

- **Linking billing** to your GCP project
- **Creating the GitHub repository** (the script pushes to it once you've created it)
- **Creating the Document AI processor** (covered in Step 2 above)

---

## Step 4 — Add permitted users

The upload and review frontend is protected by Identity-Aware Proxy (IAP). Only users you explicitly grant access can sign in.

To add a user:

1. Go to https://console.cloud.google.com/security/iap?project=YOUR_PROJECT_ID
2. Find the **mopotools-frontend** Cloud Run service
3. Click **Add Principal**
4. Enter the user's Google email address
5. Role: **IAP-Secured Web App User**
6. Click **Save**

Then set the user's role in Firestore:

1. Go to https://console.cloud.google.com/firestore?project=YOUR_PROJECT_ID
2. Navigate to the **users** collection
3. Click **Add document**
4. Document ID = the user's Firebase UID (find it in Authentication → Users)
5. Add field: `role` = `contributor` (or `admin`)

---

## Step 5 — Set up SendGrid (optional, for lint reports)

Weekly lint reports are emailed via SendGrid. If you skipped this secret:

1. Create a free account at https://sendgrid.com
2. Go to Settings → API Keys → Create API Key
3. Choose **Restricted Access** → enable **Mail Send** only
4. Run `./setup-secrets.sh` and enter the key when prompted

---

## Updating secrets later

```bash
./setup-secrets.sh
```

This prompts for each secret and adds a new version in Secret Manager. Functions pick up new versions on their next cold start (or you can force a redeploy).

---

## Updating the wiki manually

If you edit wiki pages locally and want to push without going through the upload pipeline:

```bash
git add wiki/
git commit -m "edit: update quantitative-easing page"
git push origin main
```

The Cloud Build trigger fires automatically and rebuilds the Quartz wiki site within a few minutes.

---

## Custom domain (optional)

To serve the wiki at `wiki.yourdomain.com`:

1. GCP Console → Cloud Run → mopotools-wiki → **Custom Domains**
2. Click **Add mapping** → enter your domain
3. Copy the DNS records shown and add them at your domain registrar
4. Wait for DNS propagation (up to 24 hours)
5. Update `quartz.config.ts` → `baseUrl: "wiki.yourdomain.com"` and push

---

## Architecture quick reference

```
User browser
  │
  ├── /upload  → Cloud Run: mopotools-frontend (Next.js, IAP-gated)
  │     └── PDF → Cloud Storage: raw/ bucket (object-locked)
  │           └── Pub/Sub → Cloud Workflows: mopotools-ingest
  │                 ├── Cloud Function: mopotools-extract-text  (Document AI)
  │                 └── Cloud Function: mopotools-generate-wiki (Vertex AI Gemini)
  │                       └── Staging bucket → Firestore: status=awaiting-review
  │
  ├── /review  → Cloud Run: mopotools-frontend (admin only)
  │     └── Approve → GitHub commit → Cloud Build trigger
  │                         └── Quartz build → Cloud Run: mopotools-wiki
  │
  └── /        → Cloud Run: mopotools-wiki (Quartz, public)

Cloud Scheduler (weekly) → Cloud Function: mopotools-run-lint → SendGrid email
```

---

## Troubleshooting

**`terraform apply` fails with "billing account not found"**
Link a billing account at https://console.cloud.google.com/billing/linkedaccount?project=YOUR_PROJECT_ID

**Cloud Build fails: "permission denied pushing to gcr.io"**
Run `gcloud auth configure-docker` and ensure the Cloud Build service account has `Storage Admin` on the project.

**Cloud Function deploy fails: "API not enabled"**
`deploy.sh` enables all required APIs via Terraform. If you're deploying functions manually, run:
```bash
gcloud services enable cloudfunctions.googleapis.com run.googleapis.com --project=YOUR_PROJECT_ID
```

**Wiki site shows old content after approving a paper**
Cloud Build takes 2–4 minutes to rebuild. Check progress at:
https://console.cloud.google.com/cloud-build/builds?project=YOUR_PROJECT_ID

**Sweden check failing unexpectedly**
Review the violations in Firestore under `papers/{slug}.swedenViolations`. If it's a false positive, correct the citation in the generated page via the moderator edit flow, then re-approve.

**Lint report not arriving**
Check the SendGrid activity feed at https://app.sendgrid.com/email_activity and ensure `noreply@mopotools.wiki` is not blocked. You may need to verify a sender domain in SendGrid.
