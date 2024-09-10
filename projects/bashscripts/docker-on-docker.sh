#!/bin/bash

# use the jenkins docker image jenkins/jenkins
# this info is especially for if you want docker to build docker images from jenkin!!

# install docker on docker container
apt update
apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
apt update
apt install -y docker-ce docker-ce-cli containerd.io
systemctl status docker

# after installing you must allow access to the docker sock. For this:
# step a- run docker container with mount of docker.sock:
docker run -d \
	--name jenkins_container \
	--restart always \
	-p 8080:8080 \
	-p 50000:50000 \
	-v jenkins_data:/var/jenkins_home \
	-v /var/run/docker.sock:/var/run/docker.sock \
	jenkins/jenkins:lts-jdk17

# step b- chmod 777 the sock from host (not in container) I tried adding jenkins to group docker but didnt work.
sudo chmod 777 /var/run/docker.sock
