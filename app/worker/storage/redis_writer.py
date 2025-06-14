# worker/storage/redis_writer.py
from app.common.redis_client import redis_client

def update_user_stats(user_id: str, order_value: float):
    user_key = f"user:{user_id}"
    redis_client.hincrby(user_key, "order_count", 1)
    redis_client.hincrbyfloat(user_key, "total_spend", order_value)

def update_global_stats(order_value: float):
    global_key = "global:stats"
    redis_client.hincrby(global_key, "total_orders", 1)
    redis_client.hincrbyfloat(global_key, "total_revenue", order_value)
