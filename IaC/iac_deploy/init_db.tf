resource "null_resource" "init_db" {
  depends_on = [aws_db_instance.rds_db]

  provisioner "local-exec" {
    command = <<EOT
      PGPASSWORD=Vasco.123 psql \
        --host=${aws_db_instance.rds_db.address} \
        --port=5432 \
        --username=postgres \
        --dbname=postgres \
        --file=create_database.sql
    EOT
  }

  provisioner "local-exec" {
    command = <<EOT
      echo "DB_HOST='${aws_db_instance.rds_db.address}'" > ../ml_app/.env
      echo "DB_NAME='postgres'" >> ../ml_app/.env
      echo "DB_USER='postgres'" >> ../ml_app/.env
      echo "DB_PASS='Vasco.123'" >> ../ml_app/.env
    EOT
  }

  triggers = {
    db_instance_address = aws_db_instance.rds_db.address
  }
}
