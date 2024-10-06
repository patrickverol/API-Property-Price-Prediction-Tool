resource "aws_instance" "ml_api" {
  ami = "ami-0a0d9cf81c479446a"
  instance_type = "t2.micro"
  iam_instance_profile = aws_iam_instance_profile.ec2_s3_profile.name
  vpc_security_group_ids = [aws_security_group.ml_api_sg.id]
  depends_on = [aws_s3_bucket.project_ml_bucket]

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
