AWS Serverless CRUD API

A fully serverless CRUD (Create, Read, Delete) API built using AWS Lambda, API Gateway, and DynamoDB.
This project demonstrates a simple messages API with three operations:

POST /messages → Create a message

GET /messages/{id} → Retrieve a message

DELETE /messages/{id} → Delete a message



---

 Architecture

Services used:

API Gateway – Exposes REST endpoints

Lambda – Backend logic

DynamoDB – NoSQL database for storing messages

CloudWatch – Logging & monitoring



---

 API Endpoints


POST /messages

Create a new message.

Request body:

{
  "message": "hello world"
}

Response:

{
  "id": "369d2538-22d4-4b4f-99f1-2578af6c04d8",
  "message": "hello world"
}


---

GET /messages/{id}

Fetch a single message by ID.

Example ID:
369d2538-22d4-4b4f-99f1-2578af6c04d8

Response:

{
  "id": "369d2538-22d4-4b4f-99f1-2578af6c04d8",
  "message": "hello world"
}


---

DELETE /messages/{id}

Delete a message.

Response:

{
  "message": "Message deleted",
  "id": "369d2538-22d4-4b4f-99f1-2578af6c04d8"
}


---

 Project Structure

aws-serverless-crud-api/
│
├── lambda/
│   └── lambda_function.py
│
└── README.md


---

 Deployment

This API was built manually using the AWS Console:

1. Create DynamoDB table


2. Create Lambda function


3. Connect Lambda to API Gateway


4. Configure routes & methods


5. Deploy API to a stage




---

 Future Improvements

Add PUT /messages/{id} for update

Add GET /messages to list all messages

Add CloudFormation or SAM template

Build a frontend (React or plain HTML/JS)

Add authentication with Cognito



---

 License

MIT License.