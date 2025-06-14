import boto3
from typing import Generator, Dict
from app.common.config import AWS_REGION, AWS_ENDPOINT_URL, SQS_QUEUE_NAME
from app.common.enums import SQSResponseKeys

sqs = boto3.client("sqs", region_name=AWS_REGION, endpoint_url=AWS_ENDPOINT_URL)
queue_url = sqs.get_queue_url(QueueName=SQS_QUEUE_NAME)[SQSResponseKeys.QUEUE_URL.value]


def poll_messages() -> Generator[Dict, None, None]:
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=5,
        WaitTimeSeconds=5
    )

    messages = response.get("Messages", [])
    for msg in messages:
        yield msg
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg["ReceiptHandle"])
