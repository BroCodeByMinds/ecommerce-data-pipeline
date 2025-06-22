import time
import logging
from sqs.consumer import poll_messages
from processing.order_processor import process_order
from storage.redis_writer import update_user_stats, update_global_stats
from common.constants import LogMessages

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_worker():
    logger.info(LogMessages.WORKER_STARTED)

    while True:
        for msg in poll_messages():
            result = process_order(msg["Body"])
            if result:
                user_id = result["user_id"]
                order_value = result["order_value"]

                update_user_stats(user_id, order_value)
                update_global_stats(order_value)

                logger.info(LogMessages.ORDER_PROCESSED, user_id)
        time.sleep(1)  # avoid tight polling loop

if __name__ == "__main__":
    run_worker()

