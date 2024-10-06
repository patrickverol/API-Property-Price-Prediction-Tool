resource "aws_db_instance" "rds_db" {
  allocated_storage    = 20
  engine               = "postgres"
  instance_class       = "db.t3.micro"
  db_name              = "postgres"
  username             = "postgres"
  password             = "Vasco.123"
  vpc_security_group_ids = [aws_security_group.ml_api_sg.id]
  skip_final_snapshot  = true
  publicly_accessible  = true

  tags = {
    Name = "PostgreSQL RDS"
  }
}
