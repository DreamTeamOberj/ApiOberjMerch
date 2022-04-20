from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_product,
    delete_product,
    retrieve_products,
    retrieve_products,
    update_product,
)
from app.server.models.ProductModel import (
    ErrorResponseModel,
    ResponseModel,
    ProductSchema,
    UpdateProductModel,
)

products = APIRouter()


@products.get("/product")
def read_all_products(product_id: int):
    return {"product_id": product_id}


@products.get("/product/{product_id}")
def read_product(product_id: int):
    return {"product_id": product_id}


@products.post("/product/")
async def create_product(product_id: int):
    return {"product_id": product_id}


@products.put("/product/{product_id}")
async def update_product(product_id: int):
    return {"product_id": product_id}


@products.patch("/product/{product_id}")
async def patch_product(product_id: int):
    return {"product_id": product_id}


@products.delete("/product/{product_id}")
async def delete_product(product_id: int):
    return {"product_id": product_id}
