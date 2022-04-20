from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.database import (
    add_product,
    delete_product,
    retrieve_products,
    retrieve_product,
    update_product,
)
from app.server.models.ProductModel import (
    ErrorResponseModel,
    ResponseModel,
    ProductSchema,
    UpdateProductModel,
)

productRouter = APIRouter()


@productRouter.post("/product", response_description="Product data added into the database")
async def add_product_data(product: ProductSchema = Body(...)):
    product = jsonable_encoder(product)
    new_product = await add_product(product)
    return ResponseModel(new_product, "Product added successfully.")
