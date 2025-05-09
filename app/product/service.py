import requests
from .vectorstore import ProductSearchEngine
from app.config import OLLAMA_URL, OLLAMA_MODEL

class ProductQAService:
    def __init__(self, engine: ProductSearchEngine):
        self.engine = engine

    def _build_prompt(self, query: str, products):
        prompt = "Here are some products:\n"
        for p in products:
            prompt += f"- {p['Product']} (${p['Price']})\n  {p['Features']}\n"
        prompt += f"\nUser Query: {query}\nAnswer:"
        return prompt

    def answer(self, query: str) -> str:
        top_products = self.engine.search(query)
        prompt = self._build_prompt(query, top_products)
        res = requests.post(OLLAMA_URL, json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False})
        return res.json().get("response", "").strip()
