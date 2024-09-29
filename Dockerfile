# Use the official Ubuntu image as the base
FROM ubuntu:latest

# Image maintainer (optional)
LABEL maintainer="PATRICK-VEROL"

# Update system packages and install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget unzip curl openssh-client iputils-ping

# Set the Terraform version (adjust as necessary)
ENV TERRAFORM_VERSION=1.6.5

# Download and install Terraform
RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# Create the /iac folder as a mounting point for a volume
RUN mkdir /iac
VOLUME /iac

# Create the Downloads folder and install the AWS CLI (to access AWS)
RUN mkdir Downloads && \
    cd Downloads && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

# Set the default command to execute when the container is started
CMD ["/bin/bash"]
