# ─── Cloud Storage ────────────────────────────────────────────────────────────

# Raw uploads — immutable source documents
resource "google_storage_bucket" "raw" {
  name                        = "${var.project_id}-mopotools-raw"
  location                    = var.region
  uniform_bucket_level_access = true
  force_destroy               = false

  versioning {
    enabled = true
  }

  retention_policy {
    is_locked        = true
    retention_period = 315360000 # 10 years in seconds
  }

  lifecycle_rule {
    condition { num_newer_versions = 3 }
    action    { type = "Delete" }
  }

  labels = {
    project = "mopotools"
    tier    = "raw"
  }
}

# Processed text (extracted markdown from Document AI)
resource "google_storage_bucket" "processed" {
  name                        = "${var.project_id}-mopotools-processed"
  location                    = var.region
  uniform_bucket_level_access = true
  force_destroy               = false

  versioning { enabled = true }

  labels = {
    project = "mopotools"
    tier    = "processed"
  }
}

# Staging area — AI-generated wiki pages awaiting moderator approval
resource "google_storage_bucket" "staging" {
  name                        = "${var.project_id}-mopotools-staging"
  location                    = var.region
  uniform_bucket_level_access = true
  force_destroy               = false

  # Auto-delete staging files after 30 days (approved files move to git)
  lifecycle_rule {
    condition { age = 30 }
    action    { type = "Delete" }
  }

  labels = {
    project = "mopotools"
    tier    = "staging"
  }
}

# Cloud Functions source code
resource "google_storage_bucket" "functions_source" {
  name                        = "${var.project_id}-mopotools-functions"
  location                    = var.region
  uniform_bucket_level_access = true
  force_destroy               = false

  labels = {
    project = "mopotools"
    tier    = "functions"
  }
}

# ─── Pub/Sub trigger for ingest workflow ──────────────────────────────────────

resource "google_pubsub_topic" "raw_upload" {
  name = "mopotools-raw-upload"
}

# GCS → Pub/Sub notification when a new file lands in raw/
resource "google_storage_notification" "raw_upload" {
  bucket         = google_storage_bucket.raw.name
  payload_format = "JSON_API_V1"
  topic          = google_pubsub_topic.raw_upload.id
  event_types    = ["OBJECT_FINALIZE"]

  depends_on = [google_pubsub_topic_iam_member.gcs_publisher]
}

# Allow GCS service account to publish to the topic
data "google_storage_project_service_account" "gcs_account" {}

resource "google_pubsub_topic_iam_member" "gcs_publisher" {
  topic  = google_pubsub_topic.raw_upload.id
  role   = "roles/pubsub.publisher"
  member = "serviceAccount:${data.google_storage_project_service_account.gcs_account.email_address}"
}

# ─── IAM: pipeline service account cannot delete raw objects ──────────────────

resource "google_storage_bucket_iam_member" "pipeline_raw_reader" {
  bucket = google_storage_bucket.raw.name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.pipeline.email}"
}

resource "google_storage_bucket_iam_member" "pipeline_processed_writer" {
  bucket = google_storage_bucket.processed.name
  role   = "roles/storage.objectAdmin"
  member = "serviceAccount:${google_service_account.pipeline.email}"
}

resource "google_storage_bucket_iam_member" "pipeline_staging_writer" {
  bucket = google_storage_bucket.staging.name
  role   = "roles/storage.objectAdmin"
  member = "serviceAccount:${google_service_account.pipeline.email}"
}
