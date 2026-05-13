#!/bin/bash
echo "Deploying my-devops-app to local..."
docker pull my-devops-app:latest
docker stop app 2>/dev/null || true
docker rm   app 2>/dev/null || true
docker run -d --name app -p 5000:5000 my-devops-app:latest
echo "Deployment complete."
