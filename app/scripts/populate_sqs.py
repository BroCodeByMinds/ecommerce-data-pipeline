import boto3
import json
from app.common.config import AWS_ENDPOINT_URL, AWS_REGION, SQS_QUEUE_NAME

# Create the SQS client for localstack
sqs = boto3.client("sqs", endpoint_url=AWS_ENDPOINT_URL, region_name=AWS_REGION)

# Create queue if not exists and get URL
response = sqs.create_queue(QueueName=SQS_QUEUE_NAME)
queue_url = response["QueueUrl"]

# Sample order message
sample_order = {
    "order_id": "ORD1234",
    "user_id": "U5678",
    "order_timestamp": "2024-12-13T10:00:00Z",
    "order_value": 99.99,
    "items": [
        { "product_id": "P001", "quantity": 2, "price_per_unit": 20.00 },
        { "product_id": "P002", "quantity": 1, "price_per_unit": 59.99 }
    ],
    "shipping_address": "123 Main St, Springfield",
    "payment_method": "CreditCard"
}

try:
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(sample_order)
    )
    print("Sample message sent to SQS:", response["MessageId"])
except Exception as e:
    print("Failed to send message:", str(e))


print("Sample message sent to SQS")
