provider "aws" {
    region = "ap-south-2"
}

resource "aws_s3_bucket" "demo" {
    bucket = "haleem-final-demo-bucket-2026"

    tags = {
        Environment = "Dev"
    }
}