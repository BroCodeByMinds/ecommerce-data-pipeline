from redis import Redis
from fastapi import APIRouter, Depends
from app.common.redis_client import get_redis_client
from app.web.services.stats_service import StatsService
from app.common.response_builder import ResponseBuilder
from app.common.constants import ErrorMessages, ResponseFields, StatusCodes
from app.web.models.response_models import UserStatsResponse, GlobalStatsResponse


router = APIRouter()


def get_stats_service() -> StatsService:
    redis_client: Redis = get_redis_client()
    return StatsService(redis_client)


@router.get("/users/{user_id}/stats", status_code=StatusCodes.HTTP_200_OK)
async def user_stats(user_id: str, service: StatsService = Depends(get_stats_service)):
    stats = service.get_user_stats(user_id)
    if stats is None:
        return ResponseBuilder.not_found(message=ErrorMessages.USER_NOT_FOUND)

    response_data = UserStatsResponse(
        user_id=user_id,
        order_count=int(stats.get(ResponseFields.ORDER_COUNT, 0)),
        total_spend=float(stats.get(ResponseFields.TOTAL_SPEND, 0.0)),
    )
    return ResponseBuilder.success(data=response_data)


@router.get("/stats/global", status_code=StatusCodes.HTTP_200_OK)
async def global_stats(service: StatsService = Depends(get_stats_service)):
    stats = service.get_global_stats()

    response_data = GlobalStatsResponse(
        total_orders=int(stats.get(ResponseFields.TOTAL_ORDERS, 0)),
        total_revenue=float(stats.get(ResponseFields.TOTAL_REVENUE, 0.0)),
    )
    return ResponseBuilder.success(data=response_data)
