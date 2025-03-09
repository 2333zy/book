#!/bin/bash
set -e
docker stop APP
docker rm APP
docker rmi dddbook_app:latest
docker build -t dddbook_app .
docker run -d -p  8000:8000 -v /mnt/c/users/zy/Desktop/data:/app/data --name APP dddbook_app