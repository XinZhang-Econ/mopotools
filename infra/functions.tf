# ─── Cloud Functions (2nd gen) ────────────────────────────────────────────────

locals {
  functions = {
    extract_text  = "extract-text"
    generate_wiki = "generate-wiki"
    run_lint      = "run-lint"
  }
}

# Zip and upload each function's source
data "archive_file" "extract_text" {
  type        = "zip"
  source_dir  = "${path.module}/../functions/extract-text"
  output_path = "/tmp/extract-text.zip"
}

data "archive_file" "generate_wiki" {
  type        = "zip"
  source_dir  = "${path.module}/../functions/generate-wiki"
  output_path = "/tmp/generate-wiki.zip"
}

data "archive_file" "run_lint" {
  type        = "zip"
  source_dir  = "${path.module}/../functions/run-lint"
  output_path = "/tmp/run-lint.zip"
}

resource "google_storage_bucket_object" "extract_text_src" {
  name   = "functions/extract-text-${data.archive_file.extract_text.output_md5}.zip"
  bucket = google_storage_bucket.functions_source.name
  source = data.archive_file.extract_text.output_path
}

resource "google_storage_bucket_object" "generate_wiki_src" {
  name   = "functions/generate-wiki-${data.archive_file.generate_wiki.output_md5}.zip"
  bucket = google_storage_bucket.functions_source.name
  source = data.archive_file.generate_wiki.output_path
}

resource "google_storage_bucket_object" "run_lint_src" {
  name   = "functions/run-lint-${data.archive_file.run_lint.output_md5}.zip"
  bucket = google_storage_bucket.functions_source.name
  source = data.archive_file.run_lint.output_path
}

# ── extract-text function ─────────────────────────────────────────────────────
resource "google_cloudfunctions2_function" "extract_text" {
  name     = "mopotools-extract-text"
  location = var.region

  build_config {
    runtime     = "python312"
    entry_point = "extract_text"
    source {
      storage_source {
        bucket = google_storage_bucket.functions_source.name
        object = google_storage_bucket_object.extract_text_src.name
      }
    }
  }

  service_config {
    service_account_email = google_service_account.pipeline.email
    timeout_seconds       = 540
    available_memory      = "1024M"
    max_instance_count    = 10

    environment_variables = {
      GCP_PROJECT       = var.project_id
      PROCESSED_BUCKET  = google_storage_bucket.processed.name
    }

    secret_environment_variables {
      key        = "DOCUMENT_AI_PROCESSOR_ID"
      project_id = var.project_id
      secret     = google_secret_manager_secret.secrets["document-ai-processor-id"].secret_id
      version    = "latest"
    }
  }

  depends_on = [google_project_service.apis["cloudfunctions.googleapis.com"]]
}

# ── generate-wiki function ────────────────────────────────────────────────────
resource "google_cloudfunctions2_function" "generate_wiki" {
  name     = "mopotools-generate-wiki"
  location = var.region

  build_config {
    runtime     = "python312"
    entry_point = "generate_wiki"
    source {
      storage_source {
        bucket = google_storage_bucket.functions_source.name
        object = google_storage_bucket_object.generate_wiki_src.name
      }
    }
  }

  service_config {
    service_account_email = google_service_account.pipeline.email
    timeout_seconds       = 1800  # 30 min for large papers
    available_memory      = "2048M"
    max_instance_count    = 5

    environment_variables = {
      GCP_PROJECT      = var.project_id
      STAGING_BUCKET   = google_storage_bucket.staging.name
      PROCESSED_BUCKET = google_storage_bucket.processed.name
      WIKI_REPO        = var.wiki_repo
    }

    secret_environment_variables {
      key        = "VERTEX_AI_API_KEY"
      project_id = var.project_id
      secret     = google_secret_manager_secret.secrets["vertex-ai-api-key"].secret_id
      version    = "latest"
    }
  }

  depends_on = [google_project_service.apis["cloudfunctions.googleapis.com"]]
}

# ── run-lint function ─────────────────────────────────────────────────────────
resource "google_cloudfunctions2_function" "run_lint" {
  name     = "mopotools-run-lint"
  location = var.region

  build_config {
    runtime     = "python312"
    entry_point = "run_lint"
    source {
      storage_source {
        bucket = google_storage_bucket.functions_source.name
        object = google_storage_bucket_object.run_lint_src.name
      }
    }
  }

  service_config {
    service_account_email = google_service_account.pipeline.email
    timeout_seconds       = 540
    available_memory      = "512M"
    max_instance_count    = 1

    environment_variables = {
      GCP_PROJECT    = var.project_id
      STAGING_BUCKET = google_storage_bucket.staging.name
      WIKI_REPO      = var.wiki_repo
      ADMIN_EMAIL    = var.admin_email
    }

    secret_environment_variables {
      key        = "VERTEX_AI_API_KEY"
      project_id = var.project_id
      secret     = google_secret_manager_secret.secrets["vertex-ai-api-key"].secret_id
      version    = "latest"
    }

    secret_environment_variables {
      key        = "SENDGRID_API_KEY"
      project_id = var.project_id
      secret     = google_secret_manager_secret.secrets["sendgrid-api-key"].secret_id
      version    = "latest"
    }
  }

  depends_on = [google_project_service.apis["cloudfunctions.googleapis.com"]]
}
