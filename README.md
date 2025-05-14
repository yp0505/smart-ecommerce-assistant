# 🛍️ Smart E-Commerce Assistant Chatbot

Your private AI-powered e-commerce companion built with **FastAPI**, **OLLaMA**, and clean **OOP microservices**.

---

## 🚀 Overview
A conversational chatbot that can:
- 🛒 Answer product-related questions
- 📦 Track and explain order history
- 🤖 Use a local LLM (LLaMA2 via OLLaMA) to generate human-like replies

This assistant isn't just rules-based — it's prompt-engineered with real RAG-like context passing.

---

## 🧰 Tech Stack

| Tool/Tech             | Usage                                                  |
|-----------------------|---------------------------------------------------------|
| **FastAPI**           | API framework for microservices                        |
| **Python (OOP)**      | All services built using class-based architecture       |
| **OLLaMA**            | Runs LLaMA2 locally for LLM responses                   |
| **LLaMA2**            | Used for generating product and order summaries         |
| **Custom VectorStore**| Lightweight keyword-based retrieval for product data    |
| **Pandas**            | Order dataset filtering and manipulation                |
| **Jinja2 + HTML/JS**  | Web-based UI for chat interaction                      |
| **Uvicorn**           | ASGI server                                             |

---

## 🧠 What This Chatbot Can Do

### 🔹 Product Intelligence
Ask questions like:
- "What are the top-rated guitar strings?"
- "Which products are best for beginners?"

It will use a vector store to fetch relevant items, build a custom prompt, and ask the LLM to answer like a shopping expert.

### 🔹 Order Summaries
Ask:
- "What did I order last year?"
- "Show me my recent car accessories orders"

It extracts and formats structured order data, and passes it to the LLM to explain like a human agent.

### 🔹 Multi-turn Conversations
Supports:
- Remembering intent across messages
- Awaiting Customer ID in follow-ups
- Responding naturally with OLLaMA-generated sentences

---

## 📚 Datasets Used

- **Product_Information_Dataset.csv**: 5,000+ musical product listings
- **Order_Data_Dataset.csv**: Customer purchase data including sales, dates, shipping

Used for Retrieval-Augmented Generation prompts and memory.

---

## 🧪 Sample Interactions

### Product Query:
> **User:** What are the best guitar strings for acoustic guitars?
>
> **Bot:** "The D'Addario Phosphor Bronze Strings offer a balanced tone and are highly rated by 60K+ users at just $10.99."

### Order Query:
> **User:** What is the status of my car body covers?
>
> **Bot:** "Please provide your Customer ID."
>
> **User:** 41066
>
> **Bot:** "You placed an order for 5 'Car Body Covers' on 2018-11-08 with a 'Critical' priority."

---

## 🧬 Future Scope
- Embed-based semantic vector search with FAISS or Chroma
- Multilingual support via Mistral or Gemma
- User auth, login, and order history memory
- Hosted deployment on Railway, Render, or Fly.io

---

## 🤝 Let’s Connect
This project is a foundation for **Agentic AI assistants** in e-commerce. If you're building:
- RAG agents
- Local-first LLM tools
- Conversational analytics for retail

I'd love to collab! 👇

[![GitHub](https://img.shields.io/badge/GitHub-smart--ecommerce--assistant-blue?style=for-the-badge&logo=github)](https://github.com/yp0505/smart-ecommerce-assistant)

---

> Built with ❤️ by [**Yash Pise**](https://github.com/yp0505)

#LLM #OLLaMA #GenAI #FastAPI #Python #AgenticAI #RAG #Chatbots #OpenSource #YashBuilds
