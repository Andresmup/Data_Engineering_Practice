variable "credentials" {
  description = "My Credentials"
  default     = "./keys/dataengineeringcourse-0001-f44fca6a868d.json"
}


variable "project" {
  description = "Project"
  default     = "dataengineeringcourse-0001"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default = "us-central1"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default = "demo_dataset_andres_zoomcamp_2024_1"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default = "terraform-demo-bucket_andres_zoomcamp_2024_1"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}