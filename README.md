# Render PDF: Python + FastAPI + Mangum + Selenium + AWS Lambda Container

A demo project to test the AWS Lambda container support with Python FastAPI framework. The purpose of the project is to show how to develop a REST API with FastAPI, how to build & test it locally and how to deploy it on AWS using serverless services (AWS ECR, AWS Lambda & AWS API Gateway).

## Local

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

## References

https://github.com/gbdevw/python-fastapi-aws-lambda-container 

https://www.youtube.com/watch?v=RGIM4JfsSk0&t=282s&ab_channel=pixegami

https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/

https://docs.aws.amazon.com/lambda/latest/dg/images-test.html

https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-from-alt
