from fastapi import APIRouter, Body
import pandas as pd
from .vectorstore import ProductSearchEngine
from .service import ProductQAService

router = APIRouter()

df = pd.read_csv("app/product/Product_Information_Dataset.csv").fillna("")
engine = ProductSearchEngine(df.to_dict(orient="records"))
qa = ProductQAService(engine)

@router.post("/query")
def query_product(query: str = Body(..., embed=True)):
    return {"answer": qa.answer(query)}
