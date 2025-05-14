# from fastapi import APIRouter, Body, Request
# import requests
# from app.config import PRODUCT_SERVICE_PORT, ORDER_SERVICE_PORT

# router = APIRouter()

# # 💾 In-memory session context (for now, per user IP or just globally)
# last_intent = {"intent": None, "awaiting_id": False}

# def determine_intent(query: str) -> str:
#     order_keywords = ["order", "status", "track", "shipment", "delivery", "priority"]
#     if any(word in query.lower() for word in order_keywords):
#         return "order"
#     return "product"

# @router.post("/chat")
# def chat(query: str = Body(..., embed=True)):
#     global last_intent

#     # If user just enters a customer ID or number, handle as follow-up
#     if query.strip().isdigit() and last_intent.get("intent") == "order" and last_intent.get("awaiting_id"):
#         customer_id = query.strip()
#         res = requests.get(f"http://localhost:{ORDER_SERVICE_PORT}/orders/{customer_id}")
#         last_intent["awaiting_id"] = False  # reset
#         return {"answer": res.json()["summary"]}

#     # Detect fresh intent
#     intent = determine_intent(query)
#     last_intent["intent"] = intent

#     if intent == "order":
#         customer_id = next((w for w in query.split() if w.isdigit()), None)
#         if customer_id:
#             res = requests.get(f"http://localhost:{ORDER_SERVICE_PORT}/orders/{customer_id}")
#             return {"answer": res.json()["summary"]}
#         else:
#             last_intent["awaiting_id"] = True
#             return {"answer": "Please provide your Customer ID to retrieve your order details."}
#     else:
#         res = requests.post(f"http://localhost:{PRODUCT_SERVICE_PORT}/query", json={"query": query})
#         return res.json()


from fastapi import APIRouter, Body
import requests
from app.config import PRODUCT_SERVICE_PORT, ORDER_SERVICE_PORT

router = APIRouter()
last_intent = {"intent": None, "awaiting_id": False}

def determine_intent(query: str) -> str:
    order_keywords = ["order", "status", "track", "shipment", "delivery", "priority", "recent", "details"]
    if any(word in query.lower() for word in order_keywords):
        return "order"
    return "product"

@router.post("/chat")
def chat(query: str = Body(..., embed=True)):
    global last_intent

    # If user just enters a customer ID
    if query.strip().isdigit() and last_intent.get("intent") == "order" and last_intent.get("awaiting_id"):
        last_intent["awaiting_id"] = False
        res = requests.post(f"http://localhost:{ORDER_SERVICE_PORT}/orders/query", json={"query": query})
        return res.json()

    # Detect intent
    intent = determine_intent(query)
    last_intent["intent"] = intent

    if intent == "order":
        customer_id = next((w for w in query.split() if w.isdigit()), None)
        if not customer_id:
            last_intent["awaiting_id"] = True
        res = requests.post(f"http://localhost:{ORDER_SERVICE_PORT}/orders/query", json={"query": query})
        return res.json()
    else:
        res = requests.post(f"http://localhost:{PRODUCT_SERVICE_PORT}/query", json={"query": query})
        return res.json()
