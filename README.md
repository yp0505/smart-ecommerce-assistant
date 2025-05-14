# 🛒 **Smart E-Commerce Assistant** 🤖

> A modular, AI-powered chatbot that can search products, retrieve orders, and simulate real conversations using vector search + LLM logic.

---

## 🧰 **Tech Stack**

✨ **LLM Engine**: Simulated with `PromptEngine`, compatible with local LLMs like **OLLaMA**  
🧠 **In-memory Vector DB**: TF-IDF + Cosine Similarity via `scikit-learn`  
⚡ **FastAPI**: Async, modern Python web framework  
🐍 **Python OOP**: Clean class-based structure  
📊 **Pandas**: Efficient CSV & tabular data manipulation  
📈 **scikit-learn**: Vectorization & similarity scoring  
🎨 **HTML/CSS**: Interactive local chat interface  
🔌 **Uvicorn**: ASGI web server for dev & deployment

---

## 🚀 **Key Features**

✅ Multi-turn conversational assistant with memory  
✅ Order summary and product recommendation logic  
✅ RAG-powered responses using TF-IDF retrieval  
✅ Clean OOP implementation & modular services  
✅ Intelligent prompt logic simulating an LLM agent  
✅ Lightweight and offline-friendly (OLLaMA-ready)

---

## 🧠 **How It Works**

### 🔧 Architecture

```
User ⇄ HTML UI
      ⇓
   Chat Router 🧠
     ├──→ Product Service 🔍 Vector Search
     └──→ Order Service 📦 Lookup via Customer ID
```

- **Chat Router**: Classifies queries and handles chaining/memory
- **Product Search**: Vectorizes and ranks items using TF-IDF
- **Order Lookup**: Parses order CSV and summarizes results

---

## 📚 **Datasets Used**

### 📦 Order_Data_Dataset.csv
- Customer ID
- Order Date
- Product
- Sales, Shipping Cost, Priority

_Used for:_ smart order summaries and tracking queries

### 🎸 Product_Information_Dataset.csv
- Title
- Description
- Rating, Price
- Category

_Used for:_ vector-based product search and recommendations

---

## 🔍 **Vectorization (TF-IDF + Cosine)**

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
```

`vectorstore.py` computes a sparse similarity score across product descriptions and returns the top matches. Lightweight, fast, and local.

---

## 🧠 **Prompt Engine (LLM Simulation)**

- Keeps memory of previous queries
- Asks for follow-up info (like Customer ID)
- Generates natural-sounding summaries

```python
class PromptEngine:
    def __init__(self):
        self.memory = []

    def handle_query(self, query):
        # Intent classification → Order or Product → Form response
```

---

## 💬 **Sample Interactions**

### 🔎 Product Queries
**User:** _"Best guitar strings under $15?"_  
**Bot:**
```
1. Ernie Ball Slinky ($6.99) – 4.8⭐
2. D'Addario Bronze ($10.99) – 4.7⭐
```

### 📦 Order Queries
**User:** _"What did I order last? My ID is 37077."_  
**Bot:**
```
Your order on 2018-01-02 was for 'Car Media Players'.
Total: $140 | Shipping: $4.60 | Priority: Medium
```

---

## 💻 **Run Locally**

```bash
git clone https://github.com/YOUR_USERNAME/smart-ecommerce-assistant.git
cd smart-ecommerce-assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000) and chat with your assistant.

---

## 📌 **Future Upgrades**

- 🔮 Replace PromptEngine with real OLLaMA LLM
- 🌍 Add multilingual support
- 🔐 Add login & customer profiles
- 📊 Admin dashboard to view query analytics

---

## 🎥 **Demo Video**

Check out a full walkthrough of the Smart E-Commerce Assistant:  
🔗 [Watch on Loom](https://www.loom.com/share/6bfa4d205ff54b0d81a48cfc88cd87f5?sid=7d7d7403-9584-47df-b64c-8180eb9da35c)

---

## 👨‍💻 Created By

Crafted with 💡 by [**Yash Pise**](https://github.com/yp0505)
