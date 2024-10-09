provider "google" {
  project     = var.project
  region      = var.region
}



resource "google_storage_bucket" "my_bucket" {
  name          = var.GCS_BUCKET
  location      = var.region
  storage_class = var.CLASS
  force_destroy = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }

    condition {
      age = 30
    }
  }
}

resource "google_bigquery_dataset" "raw_dataset" {
  dataset_id = var.BQ_RAW_DATASET
  project    = var.project
  location   = var.region
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.BQ_DATASET
  project    = var.project
  location   = var.region
  delete_contents_on_destroy = true
}

resource "google_bigquery_dataset" "report_dataset" {
  dataset_id = var.BQ_REPORT_DATASET
  project    = var.project
  location   = var.region
  delete_contents_on_destroy = true
}
