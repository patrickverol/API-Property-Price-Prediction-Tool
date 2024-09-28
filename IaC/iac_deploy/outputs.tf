output "instance_public_dns" {
  value = aws_instance.ml_api.public_dns
}

output "rds_endpoint" {
  value = aws_db_instance.rds_db.address
}