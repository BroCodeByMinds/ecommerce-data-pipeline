from fastapi import APIRouter, HTTPException
from app.services.stats_service import get_user_stats, get_global_stats

router = APIRouter()

@router.get("/users/{user_id}/stats")
async def user_stats(user_id: str):
    stats = get_user_stats(user_id)
    if stats is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "user_id": user_id,
        "order_count": stats["order_count"],
        "total_spend": stats["total_spend"]
    }

@router.get("/stats/global")
async def global_stats():
    stats = get_global_stats()
    return {
        "total_orders": stats["total_orders"],
        "total_revenue": stats["total_revenue"]
    }
