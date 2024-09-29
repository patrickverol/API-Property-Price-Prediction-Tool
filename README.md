<h1 align="center">
    Infrastructure and API Deployment for Machine Learning Application on AWS with Terraform
</h1>

<br>
    <div align="center">
        <a><img src="https://github.com/user-attachments/assets/524ff94a-1e8e-402f-8a56-ac1d6bec54d9"></a> 
    </div>
</br>

<div align="center">
    <a href = "https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" target="_blank"></a>
    <a href = "https://developer.hashicorp.com/terraform/docs"><img src="https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white" target="_blank"></a>
    <a href = "https://docs.aws.amazon.com/"><img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white" target="_blank"></a>
    <a href = "https://docs.docker.com/"><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" target="_blank"></a>
    <a href = "https://www.postgresql.org/docs/"><img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" target="_blank"></a>
    <a href = "https://flask.palletsprojects.com/en/3.0.x/"><img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" target="_blank"></a>
    <a href = "https://scikit-learn.org/stable/"><img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" target="_blank"></a>
    <a href = "https://pandas.pydata.org/docs/index.html"><img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" target="_blank"></a>
    <a href = "https://numpy.org/doc/"><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" target="_blank"></a>
</div> 

## About the project

This project automates the deployment of infrastructure and APIs for a machine learning application on AWS using Terraform. It provisions EC2, RDS, and S3 resources, ensuring smooth integration with the Flask backend and PostgreSQL database. The solution simplifies infrastructure management and accelerates API deployment for ML workflows.

If you want more details about how the model was trained, please acess the folder data_science, where there is a complete data science project explaining the ML model.

## Installation and configuration

  1. Make sure you have Docker Desktop installed on your computer, if not, install it according to the video below:

```bash
  https://www.youtube.com/watch?v=ZyBBv1JmnWQ
```

  2. Clone the repository in the folder you want.

```bash
  git clone https://github.com/patrickverol/API-Property-Price-Prediction-Tool
```
  3. Open the terminal or command prompt and navigate to the folder where the files are.

```bash
  cd your_folder
```
  4. Run the command below to create the Docker image

```bash
  docker build -t ml-app-terraform-image:modelo1 .
```
  5. Run the command below to create the Docker container

```bash
  docker run -dit --name ml-app-terraform -p 5000:5000 -v ./IaC:/iac ml-app-terraform-image:modelo1 /bin/bash

  # NOTE: On Windows you must replace ./IaC with the full folder path, for example: E:\Documentos_Novos\01_Projetos\Airbnb\IaC
```
  6. Go to the terminal of the container that was created and write the command below to send your credentials for AWS CLI.
  You need to do that to guarante that the Terraform can create the infrastructure using your account. Otherwise, the next steps will not working.
```bash
  aws configure

  # Access key ID:
  # Secret access key:
```
  7. Run the command below to initialize Terraform.

```bash
  terraform init
```
  8. Run the command below to see the planning of the resources that will be create.
  This step is optional, if you don't want to see that you can go to the next step.
```bash
  terraform plan
```
  9. Run the command below to create the infrastructure.
```bash
  terraform apply

  # The terraform will ask to you to confirm, just write "yes".
```
  10. Wait a few minutes until the terraform finish to create the infrastruture. 
  After that, the terraform will provide to you two outputs (like defined in the file .IaC/iac_deploy/outputs.tf)
  The first one is the public IP to acess the Flask Application.
  Copy the adress and paste in your browser, remember to add ":5000", the port that we defined in the code to acess the application. 
```bash
  # The complete address will be something like that
  http://ec2-3-147-55-96.us-east-2.compute.amazonaws.com:5000/
```
  11. If you want to acess the RDS database, install the Postgres in your computer, and send the credentials below.
  The second output, is the host adress of the RDS, witch is generated after the creation of the RDS.
  Replace <output_host_address> for the second output.
```bash
  Host name/adress: <output_host_address>
  Port: 5432
  Maintenance database: postgres
  Username:postgres
  Password: Vasco.123
```


## Contact

For questions, suggestions or feedback:

<div>
    <a href="https://www.linkedin.com/in/patrick-verol/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
    <a href = "mailto:patrickverol@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div> 
