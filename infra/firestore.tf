# ─── Firestore ────────────────────────────────────────────────────────────────

resource "google_firestore_database" "mopotools" {
  name        = "(default)"
  location_id = var.region
  type        = "FIRESTORE_NATIVE"

  depends_on = [google_project_service.apis["firestore.googleapis.com"]]
}

# Composite indexes for common query patterns

# List papers by tag + status (contributor view)
resource "google_firestore_index" "papers_by_tag_status" {
  collection = "papers"
  fields {
    field_path = "tag"
    order      = "ASCENDING"
  }
  fields {
    field_path = "status"
    order      = "ASCENDING"
  }
  fields {
    field_path = "uploadedAt"
    order      = "DESCENDING"
  }
  depends_on = [google_firestore_database.mopotools]
}

# List papers by uploader (contributor's own submissions)
resource "google_firestore_index" "papers_by_uploader" {
  collection = "papers"
  fields {
    field_path = "uploader"
    order      = "ASCENDING"
  }
  fields {
    field_path = "uploadedAt"
    order      = "DESCENDING"
  }
  depends_on = [google_firestore_database.mopotools]
}

# Moderator queue: papers awaiting review, sorted by upload time
resource "google_firestore_index" "papers_awaiting_review" {
  collection = "papers"
  fields {
    field_path = "status"
    order      = "ASCENDING"
  }
  fields {
    field_path = "uploadedAt"
    order      = "ASCENDING"
  }
  depends_on = [google_firestore_database.mopotools]
}

# ─── Firestore Security Rules ─────────────────────────────────────────────────
# Note: rules are deployed separately via firebase CLI or gcloud.
# See firestore.rules in the repo root.
