# # from fastapi import APIRouter, Body
# # import requests
# # import re
# # from app.config import PRODUCT_SERVICE_PORT, ORDER_SERVICE_PORT

# # router = APIRouter()

# # def determine_intent(query: str) -> str:
# #     order_keywords = ["order", "status", "track", "shipment", "delivery", "purchase", "bought", "customer id", "id"]
# #     if any(word in query.lower() for word in order_keywords):
# #         return "order"
# #     return "product"

# # def extract_customer_id(query: str) -> str | None:
# #     match = re.search(r"(?:customer\s*id|order\s*id|id)[^\d]*(\d{4,})", query.lower())
# #     if match:
# #         return match.group(1)
# #     return None

# # @router.post("/chat")
# # def chat(query: str = Body(..., embed=True)):
# #     intent = determine_intent(query)
    
# #     if intent == "order":
# #         customer_id = extract_customer_id(query)
# #         if customer_id:
# #             try:
# #                 res = requests.get(f"http://localhost:{ORDER_SERVICE_PORT}/orders/{customer_id}")
# #                 if res.status_code == 200:
# #                     return {"answer": res.json()["summary"]}
# #                 return {"answer": "Could not fetch order. Please check the ID."}
# #             except Exception as e:
# #                 return {"answer": f"Error contacting order service: {str(e)}"}
# #         return {"answer": "Please provide your Customer ID."}
    
# #     # fallback: assume it's a product query
# #     try:
# #         res = requests.post(f"http://localhost:{PRODUCT_SERVICE_PORT}/query", json={"query": query})
# #         return res.json()
# #     except Exception as e:
# #         return {"answer": f"Error contacting product service: {str(e)}"}


# from fastapi import APIRouter, Body
# import requests
# import re
# from app.config import PRODUCT_SERVICE_PORT, ORDER_SERVICE_PORT

# router = APIRouter()

# # Temporary in-memory state (in prod, use Redis)
# conversation_state = {}

# class ChatService:
#     def __init__(self):
#         self.state = conversation_state

#     def get_state(self, user_id="default"):
#         if user_id not in self.state:
#             self.state[user_id] = {"customer_id": None, "last_order_context": None}
#         return self.state[user_id]

#     def detect_intent(self, query: str):
#         order_keywords = ["order", "status", "shipment", "track", "recent", "id", "cell-phone", "placed", "car"]
#         if any(word in query.lower() for word in order_keywords):
#             return "order"
#         return "product"

#     def extract_customer_id(self, query: str):
#         match = re.search(r"(?:customer\s*id|id)[^\d]*(\d{4,})", query.lower())
#         return match.group(1) if match else None

#     def extract_product_name(self, query: str):
#         return query.strip().lower()

#     def handle_order_query(self, query: str, state: dict):
#         customer_id = self.extract_customer_id(query)
#         if customer_id:
#             state["customer_id"] = customer_id
#             return {"answer": f"Thanks! Got your Customer ID: {customer_id}."}

#         if not state.get("customer_id"):
#             return {"answer": "Please provide your Customer ID to retrieve your order details."}

#         # Special case: recent order
#         if "most recent" in query or "last order" in query:
#             response = requests.get(f"http://localhost:{ORDER_SERVICE_PORT}/orders/{state['customer_id']}")
#             orders = response.json().get("orders", [])
#             if orders:
#                 most_recent = orders[0]
#                 state["last_order_context"] = most_recent
#                 return {
#                     "answer": (
#                         f"Your most recent order was placed on {most_recent['Order_Date']} for "
#                         f"'{most_recent['Product']}'. The total sales amount was ${most_recent['Sales']}, "
#                         f"with a shipping cost of ${most_recent['Shipping_Cost']}. The order priority is "
#                         f"marked as '{most_recent['Order_Priority']}'.\n"
#                         f"Would you like further details or help with another order?"
#                     )
#                 }

#         # Special case: product-specific order status
#         product_match = re.search(r"status of my (.+?) order", query.lower())
#         if product_match:
#             product_name = product_match.group(1).strip()
#             response = requests.get(f"http://localhost:{ORDER_SERVICE_PORT}/orders/{state['customer_id']}")
#             orders = response.json().get("orders", [])
#             match = next((o for o in orders if product_name in o["Product"].lower()), None)
#             if match:
#                 state["last_order_context"] = match
#                 return {
#                     "answer": (
#                         f"You placed an order for {match['Quantity']} '{match['Product']}' on {match['Order_Date']} "
#                         f"with a '{match['Order_Priority']}' priority.\nIf you'd like more details, just ask!"
#                     )
#                 }
#             return {"answer": f"I couldn’t find a '{product_name}' order under your ID."}

#         # If still no match
#         return {"answer": "Let me know what specific order or product you're referring to."}

#     def handle_follow_up(self, query: str, state: dict):
#         if "recent" in query or "that one" in query:
#             last = state.get("last_order_context")
#             if last:
#                 return {
#                     "answer": (
#                         f"Your order for '{last['Product']}' placed on {last['Order_Date']} "
#                         f"had '{last['Order_Priority']}' priority and cost ${last['Sales']} + "
#                         f"${last['Shipping_Cost']} shipping."
#                     )
#                 }
#         return None

#     def handle_product_query(self, query: str):
#         res = requests.post(f"http://localhost:{PRODUCT_SERVICE_PORT}/query", json={"query": query})
#         return res.json()

#     def handle_query(self, query: str, user_id="default"):
#         state = self.get_state(user_id)

#         # Check if it's a follow-up like: "the recent one"
#         follow_up = self.handle_follow_up(query, state)
#         if follow_up:
#             return follow_up

#         # Detect and route
#         intent = self.detect_intent(query)
#         if intent == "order":
#             return self.handle_order_query(query, state)
#         else:
#             return self.handle_product_query(query)


# chat_service = ChatService()

# @router.post("/chat")
# def chat(query: str = Body(..., embed=True)):
#     return chat_service.handle_query(query)


from fastapi import APIRouter, Body, Request
import requests
from app.config import PRODUCT_SERVICE_PORT, ORDER_SERVICE_PORT

router = APIRouter()

# 💾 In-memory session context (for now, per user IP or just globally)
last_intent = {"intent": None, "awaiting_id": False}

def determine_intent(query: str) -> str:
    order_keywords = ["order", "status", "track", "shipment", "delivery", "priority"]
    if any(word in query.lower() for word in order_keywords):
        return "order"
    return "product"

@router.post("/chat")
def chat(query: str = Body(..., embed=True)):
    global last_intent

    # If user just enters a customer ID or number, handle as follow-up
    if query.strip().isdigit() and last_intent.get("intent") == "order" and last_intent.get("awaiting_id"):
        customer_id = query.strip()
        res = requests.get(f"http://localhost:{ORDER_SERVICE_PORT}/orders/{customer_id}")
        last_intent["awaiting_id"] = False  # reset
        return {"answer": res.json()["summary"]}

    # Detect fresh intent
    intent = determine_intent(query)
    last_intent["intent"] = intent

    if intent == "order":
        customer_id = next((w for w in query.split() if w.isdigit()), None)
        if customer_id:
            res = requests.get(f"http://localhost:{ORDER_SERVICE_PORT}/orders/{customer_id}")
            return {"answer": res.json()["summary"]}
        else:
            last_intent["awaiting_id"] = True
            return {"answer": "Please provide your Customer ID to retrieve your order details."}
    else:
        res = requests.post(f"http://localhost:{PRODUCT_SERVICE_PORT}/query", json={"query": query})
        return res.json()
