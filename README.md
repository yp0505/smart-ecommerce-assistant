# 🛍️ Smart E-Commerce Assistant 🤖

> Your AI-powered shopping companion built with FastAPI, OLLaMA, and modular microservices.

---

## 🔥 Overview

A multi-turn conversational chatbot that intelligently answers product and order queries for an e-commerce store. It leverages OLLaMA's LLaMA2 model for human-like responses, a lightweight in-memory vector search for product ranking, and a clean OOP codebase with microservices for scalability.

---

## 🧰 Tech Stack

| Technology        | Purpose                                      |
|------------------|----------------------------------------------|
| **FastAPI**       | Web framework for API and routing            |
| **Python (OOP)**  | Modular and clean service logic              |
| **OLLaMA**        | LLM engine for generating contextual replies |
| **LLaMA2**        | Underlying LLM model used via OLLaMA         |
| **Pandas**        | CSV-based order and product data handling    |
| **Custom VectorStore** | Keyword-based similarity search over product info |
| **HTML + JS**     | Chat UI using templates and fetch API        |
| **Uvicorn**       | ASGI server to serve the app locally         |

---

## 💡 Key Features

✅ Supports both product and order queries  
✅ Interactive UI with memory support  
✅ OLLaMA-backed dynamic product responses  
✅ Custom intent detection and session tracking  
✅ Modular microservice architecture  
✅ Easily extensible for real vector DB and auth

---

## 🧠 How It Works

### System Flow

```
User ⇄ Chat UI ⇄ FastAPI
         ⇓
       /chat → Intent Router 🧠
         ├── /product/query → TF-IDF-style search + OLLaMA
         └── /order/orders/{id} → Pandas CSV lookup
```

- **PromptEngine** builds intelligent prompts using product data
- **OrderManager** formats human-readable summaries for customers
- **ChatRouter** tracks memory and awaits IDs if needed

---

## 🎯 Prompting with OLLaMA (Zero-shot)

```text
Here are some products:
- Ernie Ball Strings ($6.99)
  Excellent tone and durability for electric guitars.
- D'Addario Bronze ($10.99)
  Smooth response for acoustic play.

User Query: Best guitar strings under $15?
Answer: ...
```

This prompt is passed to OLLaMA’s `LLaMA2` and the response is returned directly to the user.

---

## 🗂️ Microservices Breakdown

### 🔹 Chat Service (`app/chat/router.py`)
- Detects intent (order/product)
- Tracks conversation context
- Routes to appropriate backend

### 🔹 Product Service (`app/product/...`)
- Uses a vector engine to find relevant items
- Builds prompts and calls OLLaMA

### 🔹 Order Service (`app/order/...`)
- Uses Pandas to filter order data
- Summarizes last order or all orders

---

## 💬 Example Conversations

**User:** "What are the best rated guitar accessories?"  
**Bot:** "Here are some top picks: Ernie Ball Strings, Amazon A-Frame Stand, and D’Addario Bronze..."

**User:** "What did I order last?"  
**Bot:** "Please provide your Customer ID."

**User:** "37077"  
**Bot:** "You ordered 'Car Media Players' on Jan 2, 2018. Price: $140. Priority: Medium."

---

## 📦 Datasets

### `Order_Data_Dataset.csv`
- Customer_Id, Product, Order_Date, Order_Priority, Sales, Shipping_Cost

### `Product_Information_Dataset.csv`
- Product, Description, Features, Price, Rating, Category

---

## 💻 Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/smart-ecommerce-assistant.git
cd smart-ecommerce-assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000](http://localhost:8000)

🧪 Open `/docs` for Swagger testing  
🧑‍💻 Use the `/` route for the interactive HTML UI

---

## 🚀 Future Enhancements

- 🧬 Real vector DB (e.g., FAISS / Chroma)
- 🔐 User login and session profiles
- 🌍 Multilingual prompt generation
- 📈 Analytics dashboard for admin use

---

## 🎥 Demo

📽️ [Click to watch full demo on Loom](https://www.loom.com/share/6bfa4d205ff54b0d81a48cfc88cd87f5?sid=7d7d7403-9584-47df-b64c-8180eb9da35c)

---

## 👨‍💻 Author

Built with ❤️ by [**Yash Pise**](https://github.com/yp0505)
