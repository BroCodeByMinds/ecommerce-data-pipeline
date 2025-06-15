import boto3
from typing import Generator, Dict
from botocore.exceptions import ClientError
from common.config import AWS_REGION, AWS_ENDPOINT_URL, SQS_QUEUE_NAME
from common.enums import SQSResponseKeys

sqs = boto3.client("sqs", region_name=AWS_REGION, endpoint_url=AWS_ENDPOINT_URL)


def get_or_create_queue_url(queue_name: str) -> str:
    try:
        return sqs.get_queue_url(QueueName=queue_name)[SQSResponseKeys.QUEUE_URL.value]
    except sqs.exceptions.QueueDoesNotExist:
        print(f"[INFO] Queue '{queue_name}' not found. Creating it...")
        sqs.create_queue(QueueName=queue_name)
        return sqs.get_queue_url(QueueName=queue_name)[SQSResponseKeys.QUEUE_URL.value]


queue_url = get_or_create_queue_url(SQS_QUEUE_NAME)


def poll_messages() -> Generator[Dict, None, None]:
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=5,
        WaitTimeSeconds=5
    )

    messages = response.get("Messages", [])
    for msg in messages:
        yield msg
        # Remove message from the queue after processing
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg["ReceiptHandle"])
