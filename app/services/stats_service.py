# stats_Service.py
import redis
import os
from app.common.config import REDIS_HOST, REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def get_user_stats(user_id: str):
    key = f"user:{user_id}"
    if not r.exists(key):
        return None
    return r.hgetall(key)

def get_global_stats():
    key = "global:stats"
    if not r.exists(key):
        return {"total_orders": 0, "total_revenue": 0.0}
    return r.hgetall(key)
