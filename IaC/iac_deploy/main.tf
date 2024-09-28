provider "aws" {
  region = "us-east-2"
}



# S3 Bucket
resource "aws_s3_bucket" "project_ml_bucket" {
  bucket = "project-ml-369199697991-bucket" 

  # Ensure that EC2 creation waits for RDS instance to be ready
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



# EC2 instance
resource "aws_instance" "ml_api" {

  ami = "ami-0a0d9cf81c479446a"  

  instance_type = "t2.micro"

  iam_instance_profile = aws_iam_instance_profile.ec2_s3_profile.name

  vpc_security_group_ids = [aws_security_group.ml_api_sg.id]

  # Ensure that EC2 creation waits for RDS instance to be ready
  depends_on = [aws_s3_bucket.project_ml_bucket]

  # Script de inicialização
  user_data = <<-EOF
                #!/bin/bash
                sudo yum update -y
                sudo yum install -yp python3 python3-pip awscli
                sudo mkdir /ml_app
                sudo aws s3 sync s3://project-ml-369199697991-bucket /ml_app
                cd /ml_app
                sudo pip3 install flask joblib scikit-learn psycopg2-binary pydantic python-dotenv gunicorn
                nohup gunicorn -w 4 -b 0.0.0.0:5000 flask_app:app &
              EOF

  tags = {
    Name = "FlaskApp"
  }
}



# RDS Instance
resource "aws_db_instance" "rds_db" {
  allocated_storage    = 20
  engine               = "postgres"
  instance_class       = "db.t3.micro"
  db_name              = "postgres"
  username             = "postgres"
  password             = "Vasco.123"
  #parameter_group_name = "default.postgres12"      # Optional
  vpc_security_group_ids = [aws_security_group.ml_api_sg.id]
  skip_final_snapshot  = true
  publicly_accessible  = true

  tags = {
    Name = "PostgreSQL RDS"
  }
}



# Null resource to run the SQL script after RDS is created
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

  # Ensure the RDS instance is fully initialized before executing the command
  triggers = {
    db_instance_address = aws_db_instance.rds_db.address
  }
}



resource "aws_security_group" "ml_api_sg" {
  
  name        = "ml_api_sg"
  
  description = "Security Group for Flask App in EC2"

  # HTTP traffic for Flask App
  ingress {
    description = "Inbound Rule 1"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  # Gunicorn/Flask on port 5000
  ingress {
    description = "Inbound Rule 2"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # SSH access to EC2
  ingress {
    description = "Inbound Rule 3"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # PostgreSQL access for RDS
  ingress {
    description = "Inbound Rule 4"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Optionally restrict this to specific IPs
  }

  # Allow all outbound traffic
  egress {
    description = "Outbound Rule"
    from_port = 0
    to_port = 65535
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}



resource "aws_iam_role" "ec2_s3_access_role" {
  
  name = "ec2_s3_access_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_role_policy" "s3_access_policy" {
  
  name = "s3_access_policy"
  
  role = aws_iam_role.ec2_s3_access_role.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket"
        ],
        Effect = "Allow",
        Resource = [
          "${aws_s3_bucket.project_ml_bucket.arn}/*",
          "${aws_s3_bucket.project_ml_bucket.arn}"
        ]
      },
    ]
  })
}

resource "aws_iam_instance_profile" "ec2_s3_profile" {
  name = "ec2_s3_profile"
  role = aws_iam_role.ec2_s3_access_role.name
}


