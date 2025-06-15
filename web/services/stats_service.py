from redis import Redis
from typing import Optional, Dict, Any
from common.constants import ResponseFields, RedisKeys


class StatsService:
    def __init__(self, redis_client: Redis):
        self.redis = redis_client

    def get_user_stats(self, user_id: str) -> Optional[Dict[str, Any]]:
        key = RedisKeys.USER_STATS.format(user_id=user_id)
        if not self.redis.exists(key):
            return None
        return self.redis.hgetall(key)

    def get_global_stats(self) -> Dict[str, Any]:
        if not self.redis.exists(RedisKeys.GLOBAL_STATS):
            return {ResponseFields.TOTAL_ORDERS: 0, ResponseFields.TOTAL_REVENUE: 0.0}
        return self.redis.hgetall(RedisKeys.GLOBAL_STATS)
