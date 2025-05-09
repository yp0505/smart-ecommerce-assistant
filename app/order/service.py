import pandas as pd
from typing import List, Dict

class OrderManager:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_orders_by_customer(self, customer_id: str) -> List[Dict]:
        try:
            cid = int(customer_id)
        except:
            return []
        return self.df[self.df["Customer_Id"] == cid].to_dict(orient="records")

    def format_summary(self, orders: List[Dict]) -> str:
        if not orders:
            return "No orders found."
        if len(orders) == 1:
            o = orders[0]
            return f"You ordered {o['Product']} on {o['Order_Date']} (priority: {o['Order_Priority']})"
        return "Multiple orders:\n" + "\n".join(f"{i+1}. {o['Product']} on {o['Order_Date']}" for i, o in enumerate(orders))
