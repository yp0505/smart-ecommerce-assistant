from fastapi import APIRouter
import pandas as pd
from .service import OrderManager

router = APIRouter()
df = pd.read_csv("app/order/Order_Data_Dataset.csv")
manager = OrderManager(df)

@router.get("/orders/{customer_id}")
def get_orders(customer_id: str):
    orders = manager.get_orders_by_customer(customer_id)
    return {"summary": manager.format_summary(orders), "orders": orders}
