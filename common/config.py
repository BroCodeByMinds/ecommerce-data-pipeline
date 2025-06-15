import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")  # Will override to 'redis' if provided in environment
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

SQS_QUEUE_NAME = os.getenv("SQS_QUEUE_NAME", "orders-queue")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL", "http://localstack:4566")
