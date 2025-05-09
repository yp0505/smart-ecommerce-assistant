# from fastapi import FastAPI
# from app.chat.router import router as chat_router
# from app.product.routes import router as product_router
# from app.order.routes import router as order_router
# from app.config import CHAT_SERVICE_PORT

# app = FastAPI(title="Ecommerce Chatbot")
# app.include_router(chat_router, prefix="")
# app.include_router(product_router, prefix="/product")
# app.include_router(order_router, prefix="/order")

# Run with: uvicorn app.main:app --port 8000 --reload
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.chat.router import router as chat_router
from app.order.routes import router as order_router
from app.product.routes import router as product_router

app = FastAPI(title="Ecommerce Chatbot")

# Add templates folder for UI
templates = Jinja2Templates(directory="app/templates")

app.include_router(chat_router, prefix="")
app.include_router(order_router, prefix="/order")
app.include_router(product_router, prefix="/product")

@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})
