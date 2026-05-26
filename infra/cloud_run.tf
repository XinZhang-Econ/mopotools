# ─── Cloud Run Services ───────────────────────────────────────────────────────

# 1. Frontend: upload form + moderator UI (Next.js)
resource "google_cloud_run_v2_service" "frontend" {
  name     = "mopotools-frontend"
  location = var.region

  template {
    service_account = google_service_account.frontend.email

    containers {
      # Placeholder image — replaced by deploy.sh after Docker build
      image = "us-docker.pkg.dev/cloudrun/container/hello"

      env {
        name  = "GCP_PROJECT"
        value = var.project_id
      }
      env {
        name  = "RAW_BUCKET"
        value = google_storage_bucket.raw.name
      }
      env {
        name  = "STAGING_BUCKET"
        value = google_storage_bucket.staging.name
      }
      env {
        name  = "WIKI_REPO"
        value = var.wiki_repo
      }
      env {
        name = "GITHUB_TOKEN"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.secrets["github-token"].secret_id
            version = "latest"
          }
        }
      }

      resources {
        limits = {
          cpu    = "1"
          memory = "512Mi"
        }
      }
    }

    scaling {
      min_instance_count = 0
      max_instance_count = 3
    }
  }

  depends_on = [google_project_service.apis["run.googleapis.com"]]
}

# IAP users are added manually per-person via GCP Console or gcloud:
#   gcloud projects add-iam-policy-binding PROJECT_ID \
#     --member="user:EMAIL" --role="roles/iap.httpsResourceAccessor"
# Domain-level bindings only work for Google Workspace domains, not gmail.com.

# 2. Wiki site: Quartz static site
resource "google_cloud_run_v2_service" "wiki_site" {
  name     = "mopotools-wiki"
  location = var.region

  template {
    service_account = google_service_account.wiki_site.email

    containers {
      # Placeholder image — replaced by deploy.sh after Docker build
      image = "us-docker.pkg.dev/cloudrun/container/hello"

      resources {
        limits = {
          cpu    = "1"
          memory = "512Mi"
        }
      }
    }

    scaling {
      min_instance_count = 0
      max_instance_count = 5
    }
  }

  depends_on = [google_project_service.apis["run.googleapis.com"]]
}

# Wiki site can be public (no IAP) — adjust if access should be restricted
resource "google_cloud_run_v2_service_iam_member" "wiki_public" {
  project  = var.project_id
  location = var.region
  name     = google_cloud_run_v2_service.wiki_site.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}

# ─── Cloud CDN (via Load Balancer) for wiki site ──────────────────────────────

resource "google_compute_region_network_endpoint_group" "wiki_neg" {
  name                  = "mopotools-wiki-neg"
  network_endpoint_type = "SERVERLESS"
  region                = var.region

  cloud_run {
    service = google_cloud_run_v2_service.wiki_site.name
  }
}

resource "google_compute_backend_service" "wiki_backend" {
  name        = "mopotools-wiki-backend"
  protocol    = "HTTPS"
  port_name   = "http"
  timeout_sec = 30

  backend {
    group = google_compute_region_network_endpoint_group.wiki_neg.id
  }

  cdn_policy {
    cache_mode                   = "CACHE_ALL_STATIC"
    default_ttl                  = 3600
    max_ttl                      = 86400
    serve_while_stale            = 86400
    negative_caching             = true
    signed_url_cache_max_age_sec = 0
  }

  enable_cdn = true
}
