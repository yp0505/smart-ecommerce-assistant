from fastapi import APIRouter, Body
import requests
from app.config import PRODUCT_SERVICE_PORT, ORDER_SERVICE_PORT

router = APIRouter()

def determine_intent(query: str) -> str:
    order_keywords = ["order", "status", "track", "shipment", "delivery"]
    if any(word in query.lower() for word in order_keywords):
        return "order"
    return "product"


@router.post("/chat")
def chat(query: str = Body(..., embed=True)):
    intent = determine_intent(query)
    if intent == "order":
        # extract ID if mentioned
        customer_id = next((w for w in query.split() if w.isdigit()), None)
        if customer_id:
            res = requests.get(f"http://localhost:{ORDER_SERVICE_PORT}/orders/{customer_id}")
            return {"answer": res.json()["summary"]}
        return {"answer": "Please provide your Customer ID."}
    else:
        res = requests.post(f"http://localhost:{PRODUCT_SERVICE_PORT}/query", json={"query": query})
        return res.json()
