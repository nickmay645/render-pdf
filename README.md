## Python + FastAPI + Mangum + AWS Lambda Container

A demo project to test the AWS Lambda container support with Python FastAPI framework. The purpose of the project is to show how to develop a REST API with FastAPI, how to build & test it locally and how to deploy it on AWS using serverless services (AWS ECR, AWS Lambda & AWS API Gateway).

### Build a the local container

```
docker build -t pdf-render . 
```

### Run the local container
```
docker run -p 8000:8000 pdf-render:latest
```