# worker/main.py
from app.worker.sqs.consumer import poll_messages
from app.worker.processing.order_processor import process_order
from app.worker.storage.redis_writer import update_user_stats, update_global_stats

def run_worker():
    print("Worker started polling SQS...")
    for msg in poll_messages():
        result = process_order(msg["Body"])
        if result:
            user_id = result["user_id"]
            order_value = result["order_value"]
            update_user_stats(user_id, order_value)
            update_global_stats(order_value)
            print(f"Processed order for user {user_id}")

if __name__ == "__main__":
    run_worker()
