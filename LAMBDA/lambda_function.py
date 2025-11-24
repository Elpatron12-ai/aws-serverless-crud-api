import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("messages")

def lambda_handler(event, context):
    http_method = event.get("httpMethod")
    path_params = event.get("pathParameters") or {}
    body = {}

    if event.get("body"):
        try:
            body = json.loads(event["body"])
        except:
            body = {}

    if http_method == "POST":
        message_id = str(uuid.uuid4())
        message_text = body.get("message", "")

        table.put_item(Item={"id": message_id, "message": message_text})

        return {"statusCode": 200, "body": json.dumps({"id": message_id, "message": message_text})}

    elif http_method == "GET" and "id" in path_params:
        item_id = path_params["id"]
        result = table.get_item(Key={"id": item_id})

        if "Item" not in result:
            return {"statusCode": 404, "body": json.dumps({"error": "Message not found"})}

        return {"statusCode": 200, "body": json.dumps(result["Item"])}

    elif http_method == "DELETE" and "id" in path_params:
        item_id = path_params["id"]
        table.delete_item(Key={"id": item_id})

        return {"statusCode": 200, "body": json.dumps({"message": "Message deleted", "id": item_id})}

    return {"statusCode": 400, "body": json.dumps({"error": "Unsupported HTTP method"})}