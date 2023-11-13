#! /usr/bin/bash

sudo yum install docker -y
sudo service docker start
sudo service docker status
sudo usermod -a -G docker ec2-user
newgrp docker
docker — version
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 318746479556.dkr.ecr.us-east-1.amazonaws.com
docker pull 318746479556.dkr.ecr.us-east-1.amazonaws.com/sb-training
docker container run -d -p 8090:8090 318746479556.dkr.ecr.us-east-1.amazonaws.com/sb-training 
INSTANCE_ID=$(ec2-metadata -i | awk '{print $2}')
aws ec2 create-tags --resources $INSTANCE_ID --tags Key=Name,Value=sb-instance-$(hostname)