# worker/sqs/consumer.py
import boto3
import json
from app.common.config import AWS_REGION, AWS_ENDPOINT_URL, SQS_QUEUE_NAME

sqs = boto3.client("sqs", region_name=AWS_REGION, endpoint_url=AWS_ENDPOINT_URL)
queue_url = sqs.get_queue_url(QueueName=SQS_QUEUE_NAME)["QueueUrl"]

def poll_messages():
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=5,
        WaitTimeSeconds=5
    )

    messages = response.get("Messages", [])
    for msg in messages:
        yield msg
        # Delete after processing (to avoid re-processing)
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg["ReceiptHandle"])
