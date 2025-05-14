# from fastapi import APIRouter
# import pandas as pd
# from .service import OrderManager

# router = APIRouter()
# df = pd.read_csv("app/order/Order_Data_Dataset.csv")
# manager = OrderManager(df)

# @router.get("/orders/{customer_id}")
# def get_orders(customer_id: str):
#     orders = manager.get_orders_by_customer(customer_id)
#     return {"summary": manager.format_summary(orders), "orders": orders}


from fastapi import APIRouter, Body
import pandas as pd
from .service import OrderManager

router = APIRouter()
df = pd.read_csv("app/order/Order_Data_Dataset.csv")
manager = OrderManager(df)

@router.get("/orders/{customer_id}")
def get_orders(customer_id: str):
    orders = manager.get_orders_by_customer(customer_id)
    return {"summary": manager.format_with_llm(f"Give me my recent order details", orders), "orders": orders}

@router.post("/orders/query")
def query_orders(query: str = Body(..., embed=True)):
    # Detect if user asked about high priority orders
    if "high priority" in query.lower():
        orders = manager.get_high_priority_orders()
    else:
        # Try to extract Customer ID from the query
        customer_id = next((w for w in query.split() if w.isdigit()), None)
        if customer_id:
            orders = manager.get_orders_by_customer(customer_id)
        else:
            return {"answer": "Please provide your Customer ID."}

    response = manager.format_with_llm(query, orders)
    return {"answer": response}
