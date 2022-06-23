from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    add_product,
    delete_product,
    retrieve_products,
    retrieve_product,
    update_product,
)
from server.models.ProductModel import (
    ErrorResponseModel,
    ResponseModel,
    ProductSchema,
    UpdateProductModel,
)

productRouter = APIRouter()


@productRouter.post("/products", response_description="Product data added into the database")
async def add_product_data(product: ProductSchema = Body(...)):
    product = jsonable_encoder(product)
    new_product = await add_product(product)
    return ResponseModel(new_product, "Product added successfully.")


@productRouter.get("/products", response_description="Products retrieved")
async def get_products():
    products = await retrieve_products()
    return products


@productRouter.get("/products/{id}", response_description="Product data retrieved")
async def get_product_data(id):
    product = await retrieve_product(id)
    return product


@productRouter.put("/products/{id}")
async def update_product_data(id: str, req: UpdateProductModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_product = await update_product(id, req)
    return updated_product


@productRouter.delete("/products/{id}", response_description="Product data deleted from the database")
async def delete_product_data(id: str):
    deleted_product = await delete_product(id)
    return deleted_product
