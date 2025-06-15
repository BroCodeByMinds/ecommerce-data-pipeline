# app/common/constants.py

class RedisKeys:
    USER_STATS = "user:{user_id}"
    GLOBAL_STATS = "global:stats"


class ErrorMessages:
    USER_NOT_FOUND = "User not found"


class ResponseFields:
    ORDER_COUNT = "order_count"
    TOTAL_SPEND = "total_spend"
    TOTAL_ORDERS = "total_orders"
    TOTAL_REVENUE = "total_revenue"


class StatusCodes:
    HTTP_200_OK = 200
    HTTP_404_NOT_FOUND = 404
    HTTP_500_INTERNAL_SERVER_ERROR = 500
    HTTP_400_BAD_REQUEST = 400


class Messages:
    SUCCESS = "Success"
    USER_NOT_FOUND = "User not found"
    RESOURCE_NOT_FOUND = "Resource not found"
    INTERNAL_SERVER_ERROR = "Internal server error"
    BAD_REQUEST = "Bad request"



class ResponseStatus:
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"


class SQSKeys:
    QUEUE_URL = "QueueUrl"
    MESSAGE_ID = "MessageId"

class LogMessages:
    SQS_SEND_SUCCESS = "Message sent to SQS. Message ID: %s"
    SQS_SEND_FAILURE = "Failed to send message to SQS: %s"
    PROCESSING_ERROR = "Failed to process order: %s"
    INVALID_ORDER = "Invalid order received: %s"
    WORKER_STARTED = "Worker started polling SQS..."
    ORDER_PROCESSED = "Processed order for user %s"

class OrderFields:
    ORDER_ID = "order_id"
    USER_ID = "user_id"
    ORDER_VALUE = "order_value"
    ITEMS = "items"
    QUANTITY = "quantity"
    PRICE_PER_UNIT = "price_per_unit"
    ORDER_TIMESTAMP = "order_timestamp"
