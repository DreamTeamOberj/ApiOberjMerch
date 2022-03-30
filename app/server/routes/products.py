from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

products = APIRouter()


@products.get("/product")
def read_all_products(product_id: int):
    return {"product_id": product_id}


@products.get("/product/{product_id}")
def read_product(product_id: int):
    return {"product_id": product_id}
