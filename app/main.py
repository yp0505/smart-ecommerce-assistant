from fastapi import FastAPI
from app.chat.router import router as chat_router
from app.product.routes import router as product_router
from app.order.routes import router as order_router
from app.config import CHAT_SERVICE_PORT

app = FastAPI(title="Ecommerce Chatbot")
app.include_router(chat_router, prefix="")
app.include_router(product_router, prefix="/product")
app.include_router(order_router, prefix="/order")

# Run with: uvicorn app.main:app --port 8000 --reload
