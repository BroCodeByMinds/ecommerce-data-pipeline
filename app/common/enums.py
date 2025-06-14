from enum import Enum

from app.common.constants import SQSKeys


class SQSResponseKeys(str, Enum):
    QUEUE_URL = SQSKeys.QUEUE_URL
    MESSAGE_ID = SQSKeys.MESSAGE_ID


class LogMessages(str, Enum):
    MESSAGE_SENT = "Message sent to SQS. Message ID: %s"
    MESSAGE_FAILED = "Failed to send message to SQS: %s"
