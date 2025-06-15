import redis
from typing import Optional
from common.config import REDIS_HOST, REDIS_PORT

_redis_client: Optional[redis.Redis] = None

def get_redis_client() -> redis.Redis:
    """
    Returns a Redis client. Uses singleton pattern to initialize only once.
    """
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )
    return _redis_client
