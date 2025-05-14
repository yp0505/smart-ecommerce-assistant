import pandas as pd
from typing import List, Dict
import requests
from app.config import OLLAMA_URL, OLLAMA_MODEL

class OrderManager:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_orders_by_customer(self, customer_id: str) -> List[Dict]:
        try:
            cid = int(customer_id)
        except:
            return []
        return self.df[self.df["Customer_Id"] == cid].to_dict(orient="records")

    def get_high_priority_orders(self, limit: int = 5) -> List[Dict]:
        hp = self.df[self.df["Order_Priority"].str.lower() == "high"]
        recent = hp.sort_values("Order_Date", ascending=False).head(limit)
        return recent.to_dict(orient="records")

    def format_with_llm(self, query: str, orders: List[Dict]) -> str:
        if not orders:
            return "No orders found for your query."

        prompt = (
            "You are a helpful e-commerce assistant.\n"
            "Below are matching customer orders. Use this information to answer the user's query.\n"
            "DO NOT fabricate or suggest any new products. ONLY use real order details provided.\n\n"
            "Order Records:\n"
        )

        for i, o in enumerate(orders, 1):
            prompt += (
                f"{i}. Product: {o['Product']}, Quantity: {o['Quantity']}, Order Date: {o['Order_Date']}, "
                f"Sales: ${o['Sales']}, Shipping Cost: ${o['Shipping_Cost']}, "
                f"Priority: {o['Order_Priority']}, Customer ID: {o['Customer_Id']}\n"
            )

        prompt += f"\nUser Query: {query}\n\n"
        prompt += "Answer like a real agent: concise, helpful, grounded in the data only."

        res = requests.post(
            OLLAMA_URL,
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
        )
        return res.json().get("response", "Sorry, no valid response.").strip()





