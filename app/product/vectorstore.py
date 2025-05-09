import pandas as pd
from typing import List, Dict

class ProductSearchEngine:
    def __init__(self, data: List[Dict]):
        self.data = data

    def _concat_fields(self, product: Dict) -> str:
        return " ".join(str(product.get(k, "")) for k in ["Product", "Product_Category", "Description", "Features"])

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        query = query.lower()
        results = []
        for item in self.data:
            text = self._concat_fields(item).lower()
            score = sum(word in text for word in query.split())
            if score:
                results.append((score, item))
        results.sort(reverse=True)
        return [item[1] for item in results[:top_k]]
