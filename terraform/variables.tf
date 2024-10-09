variable "project" {
  type        = string
  description = "GCP project"
}

variable "region" {
  type        = string
  default     = "us-central1"
  description = "Region used in this project"
}


variable "GCS_BUCKET" {
    type = string
    description = "GCS bucket for storing raw Steam data files"
}

variable "CLASS" {
  type        = string
  description = "bucket class"
}

variable "BQ_RAW_DATASET" {
  type        = string
  description = "BigQuery dataset to hold the raw data"
}

variable "BQ_DATASET" {
  type        = string
  description = "BigQuery dataset for cleaned data modeled in a star schema "
}

variable "BQ_REPORT_DATASET" {
  type        = string
  description = "BigQuery dataset for report views"
}