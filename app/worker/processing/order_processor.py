# worker/processing/order_processor.py
import json

def is_valid_order(order: dict) -> bool:
    try:
        if not all(k in order for k in ("user_id", "order_id", "order_value", "items")):
            return False
        calculated_total = sum(item["quantity"] * item["price_per_unit"] for item in order["items"])
        return abs(calculated_total - order["order_value"]) < 0.01  # float-safe
    except Exception:
        return False

def process_order(raw_msg: str):
    try:
        order = json.loads(raw_msg)
        if not is_valid_order(order):
            print(f"Invalid order: {order.get('order_id')}")
            return None
        
        return {
            "user_id": order["user_id"],
            "order_value": order["order_value"],
            "order_timestamp": order["order_timestamp"]
        }
    except Exception as e:
        print("Failed to process order:", e)
        return None
