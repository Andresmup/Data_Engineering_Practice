terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.33.0"
    }
  }
}

provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region     = var.region
}


resource "aws_s3_bucket" "terraform_andres_s3" {
  bucket = var.bucket_name
  acl    = "private"
  tags = {
    Name        = "Terraform bucket"
    Environment = "Dev"
  }
  versioning {
    enabled = false
  }
}
