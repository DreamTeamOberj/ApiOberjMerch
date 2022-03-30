from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/product")
def read_all_products(product_id: int, q: Optional[str] = None):
    return {"product_id": product_id, "q": q}

@app.get("/product/{product_id}")
def read_product(product_id: int, q: Optional[str] = None):
    return {"product_id": product_id, "q": q}