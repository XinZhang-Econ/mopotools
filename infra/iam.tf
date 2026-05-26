# ─── Service Accounts ─────────────────────────────────────────────────────────

# Pipeline SA: used by Cloud Functions and Cloud Workflows
resource "google_service_account" "pipeline" {
  account_id   = "mopotools-pipeline"
  display_name = "MoPoTools Pipeline Service Account"
}

# Frontend SA: used by Cloud Run upload/moderator UI
resource "google_service_account" "frontend" {
  account_id   = "mopotools-frontend"
  display_name = "MoPoTools Frontend Service Account"
}

# Wiki site SA: used by Quartz Cloud Run service
resource "google_service_account" "wiki_site" {
  account_id   = "mopotools-wiki-site"
  display_name = "MoPoTools Wiki Site Service Account"
}

# ─── Project-level IAM bindings ───────────────────────────────────────────────

# Pipeline: Document AI, Vertex AI, Firestore, Workflows invoker
resource "google_project_iam_member" "pipeline_roles" {
  for_each = toset([
    "roles/documentai.editor",
    "roles/aiplatform.user",
    "roles/datastore.user",
    "roles/workflows.invoker",
    "roles/secretmanager.secretAccessor",
    "roles/logging.logWriter",
  ])
  project = var.project_id
  role    = each.value
  member  = "serviceAccount:${google_service_account.pipeline.email}"
}

# Frontend: Firestore, sign Storage URLs, read staging
resource "google_project_iam_member" "frontend_roles" {
  for_each = toset([
    "roles/datastore.user",
    "roles/iam.serviceAccountTokenCreator",
    "roles/secretmanager.secretAccessor",
    "roles/logging.logWriter",
  ])
  project = var.project_id
  role    = each.value
  member  = "serviceAccount:${google_service_account.frontend.email}"
}

# Wiki site: read staging bucket (to serve pages before commit, if needed)
resource "google_project_iam_member" "wiki_site_roles" {
  for_each = toset([
    "roles/logging.logWriter",
  ])
  project = var.project_id
  role    = each.value
  member  = "serviceAccount:${google_service_account.wiki_site.email}"
}

# ─── Secret Manager secrets ───────────────────────────────────────────────────

resource "google_secret_manager_secret" "secrets" {
  for_each  = toset([
    "vertex-ai-api-key",
    "document-ai-processor-id",
    "github-token",
    "sendgrid-api-key",
    "iap-client-secret",
  ])
  secret_id = each.value
  replication {
    auto {}
  }
  depends_on = [google_project_service.apis["secretmanager.googleapis.com"]]
}

# Placeholder secret versions — allows functions to deploy before real values are set.
# Run ./setup-secrets.sh to overwrite these with real values.
resource "google_secret_manager_secret_version" "placeholders" {
  for_each    = google_secret_manager_secret.secrets
  secret      = each.value.id
  secret_data = "placeholder-replace-with-setup-secrets-sh"

  lifecycle {
    # Prevent Terraform from reverting real values back to placeholder on next apply
    ignore_changes = [secret_data]
  }
}

# Pipeline can access its own secrets only
resource "google_secret_manager_secret_iam_member" "pipeline_secrets" {
  for_each  = toset(["vertex-ai-api-key", "document-ai-processor-id"])
  secret_id = google_secret_manager_secret.secrets[each.value].secret_id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.pipeline.email}"
}

resource "google_secret_manager_secret_iam_member" "frontend_github" {
  secret_id = google_secret_manager_secret.secrets["github-token"].secret_id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.frontend.email}"
}

resource "google_secret_manager_secret_iam_member" "lint_sendgrid" {
  secret_id = google_secret_manager_secret.secrets["sendgrid-api-key"].secret_id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.pipeline.email}"
}
