resource "aws_s3_bucket" "project_ml_bucket" {
  bucket = "project-ml-369199697991-bucket" 

  depends_on = [aws_db_instance.rds_db, null_resource.init_db]

  tags = {
    Name        = "Project ML Bucket"
    Environment = "Projeto Airbnb"
  }

  provisioner "local-exec" {
    command = "${path.module}/upload_to_s3.sh"
  }

  provisioner "local-exec" {
    when    = destroy
    command = "aws s3 rm s3://project-ml-369199697991-bucket --recursive"
  }
}
