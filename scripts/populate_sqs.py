import json
import sys
import logging
import boto3
from common.constants import LogMessages
from botocore.exceptions import BotoCoreError, ClientError
from common.config import AWS_ENDPOINT_URL, AWS_REGION, SQS_QUEUE_NAME
from common.enums import SQSResponseKeys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_sqs_client():
    return boto3.client("sqs", endpoint_url=AWS_ENDPOINT_URL,
                        aws_access_key_id="dummy",          
                        aws_secret_access_key="dummy",
                        region_name=AWS_REGION)


def get_queue_url(sqs_client) -> str:
    response = sqs_client.create_queue(QueueName=SQS_QUEUE_NAME)
    return response[SQSResponseKeys.QUEUE_URL.value]


def get_sample_order() -> dict:
    return {
        "order_id": "ORD1235",
        "user_id": "U0003",
        "order_timestamp": "2024-12-13T10:00:00Z",
        "order_value": 60.00,
        "items": [
            {"product_id": "P003", "quantity": 1, "price_per_unit": 35.00},
            {"product_id": "P004", "quantity": 1, "price_per_unit": 25.00}
        ],
        "shipping_address": "123 Main St, Springfield",
        "payment_method": "CreditCard"
    }


def send_order_to_sqs(sqs_client, queue_url: str, order_data: dict):
    try:
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(order_data)
        )
        logger.info(LogMessages.SQS_SEND_SUCCESS, response[SQSResponseKeys.MESSAGE_ID.value])
    except (BotoCoreError, ClientError) as e:
        logger.error(LogMessages.SQS_SEND_FAILURE, str(e))
        sys.exit(1)


def main():
    sqs_client = get_sqs_client()
    queue_url = get_queue_url(sqs_client)
    order = get_sample_order()
    send_order_to_sqs(sqs_client, queue_url, order)


if __name__ == "__main__":
    main()
