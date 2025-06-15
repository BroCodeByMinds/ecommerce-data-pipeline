from common.redis_client import get_redis_client
from common.constants import RedisKeys, ResponseFields


def update_user_stats(user_id: str, order_value: float):
    user_key = RedisKeys.USER_STATS.format(user_id=user_id)
    redis_client = get_redis_client()
    redis_client.hincrby(user_key, ResponseFields.ORDER_COUNT, 1)
    redis_client.hincrbyfloat(user_key, ResponseFields.TOTAL_SPEND, order_value)


def update_global_stats(order_value: float):
    global_key = RedisKeys.GLOBAL_STATS
    redis_client = get_redis_client()
    redis_client.hincrby(global_key, ResponseFields.TOTAL_ORDERS, 1)
    redis_client.hincrbyfloat(global_key, ResponseFields.TOTAL_REVENUE, order_value)
