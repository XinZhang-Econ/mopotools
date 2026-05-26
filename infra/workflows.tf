# ─── Cloud Workflows ──────────────────────────────────────────────────────────

resource "google_workflows_workflow" "ingest" {
  name            = "mopotools-ingest"
  region          = var.region
  service_account = google_service_account.pipeline.email
  source_contents = file("${path.module}/../workflows/ingest.yaml")

  depends_on = [google_project_service.apis["workflows.googleapis.com"]]
}

# Pub/Sub subscription that triggers the workflow on new raw uploads
resource "google_pubsub_subscription" "raw_upload_workflow" {
  name  = "mopotools-raw-upload-workflow"
  topic = google_pubsub_topic.raw_upload.id

  push_config {
    push_endpoint = "https://workflowexecutions.googleapis.com/v1/projects/${var.project_id}/locations/${var.region}/workflows/${google_workflows_workflow.ingest.name}/executions"

    oidc_token {
      service_account_email = google_service_account.pipeline.email
    }
  }

  ack_deadline_seconds = 60
  retry_policy {
    minimum_backoff = "60s"
    maximum_backoff = "600s"
  }
}

# ─── Cloud Scheduler ──────────────────────────────────────────────────────────

# Weekly lint job — Mondays at 08:00 UTC
resource "google_cloud_scheduler_job" "lint" {
  name      = "mopotools-lint-weekly"
  schedule  = "0 8 * * 1"
  time_zone = "UTC"
  region    = var.region

  http_target {
    http_method = "POST"
    uri         = google_cloudfunctions2_function.run_lint.url

    oidc_token {
      service_account_email = google_service_account.pipeline.email
    }

    body = base64encode(jsonencode({
      wiki_repo    = var.wiki_repo
      admin_email  = var.admin_email
    }))

    headers = {
      "Content-Type" = "application/json"
    }
  }

  depends_on = [google_project_service.apis["cloudscheduler.googleapis.com"]]
}
