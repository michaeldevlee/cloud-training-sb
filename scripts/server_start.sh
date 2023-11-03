#!/usr/bin/env bash
cd /home/ec2-user/server
sudo java -jar *.jar --spring.config.name=spring-boot-demo --spring.profiles.active=local > /dev/null 2> /dev/null < /dev/null &