from pydantic import BaseModel


class UserStatsResponse(BaseModel):
    user_id: str
    order_count: int
    total_spend: float


class GlobalStatsResponse(BaseModel):
    total_orders: int
    total_revenue: float