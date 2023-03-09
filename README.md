## Render PDF: Python + FastAPI + Mangum + AWS Lambda Container

A demo project to test the AWS Lambda container support with Python FastAPI framework. The purpose of the project is to demonstrate a REST API with FastAPI, how to build & test it locally and how to deploy it on AWS using serverless services (AWS ECR, AWS Lambda & AWS API Gateway).

### Build a the local container

```
docker build -t pdf-render . 
```

### Run the local container
```
docker run -p 8000:8000 pdf-render:latest
```

### Test the API
In your browser you can navigate to 
```
http://0.0.0.0:8000/docs
```
to see capabilities

To render a page into base64 encoded bytes of a PDF you can use:
```
http://0.0.0.0:8000/render?url=https:www.google.com&proxy_url=http://USER:PASS@DOMAIN:PORT
```
