import json
import logging
from typing import Optional, Dict
from app.common.constants import LogMessages, OrderFields

logger = logging.getLogger(__name__)


def is_valid_order(order: dict) -> bool:
    try:
        required_fields = (
            OrderFields.USER_ID,
            OrderFields.ORDER_ID,
            OrderFields.ORDER_VALUE,
            OrderFields.ITEMS
        )
        if not all(k in order for k in required_fields):
            return False

        calculated_total = sum(
            item[OrderFields.QUANTITY] * item[OrderFields.PRICE_PER_UNIT]
            for item in order[OrderFields.ITEMS]
        )
        return abs(calculated_total - order[OrderFields.ORDER_VALUE]) < 0.01
    except Exception as e:
        logger.warning(LogMessages.PROCESSING_ERROR, e)
        return False


def process_order(raw_msg: str) -> Optional[Dict]:
    try:
        order = json.loads(raw_msg)
        if not is_valid_order(order):
            logger.warning(LogMessages.INVALID_ORDER, order.get(OrderFields.ORDER_ID))
            return None

        return {
            OrderFields.USER_ID: order[OrderFields.USER_ID],
            OrderFields.ORDER_VALUE: order[OrderFields.ORDER_VALUE],
            OrderFields.ORDER_TIMESTAMP: order[OrderFields.ORDER_TIMESTAMP]
        }
    except Exception as e:
        logger.error(LogMessages.PROCESSING_ERROR, e)
        return None
