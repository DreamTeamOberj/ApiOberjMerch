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


@productRouter.get("/products", response_description="Products retrieved")
async def get_students():
    products = await retrieve_products()
    if products:
        return ResponseModel(products, "Products data retrieved successfully")
    return ResponseModel(products, "Empty list returned")


@productRouter.get("/product/{id}", response_description="Student data retrieved")
async def get_product_data(id):
    product = await retrieve_product(id)
    if product:
        return ResponseModel(product, "Product data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Product doesn't exist.")


@productRouter.put("/product/{id}")
async def update_product_data(id: str, req: UpdateProductModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_product = await update_product(id, req)
    if updated_product:
        return ResponseModel(
            "Product with ID: {} name update is successful".format(id),
            "Product name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


@productRouter.delete("/product/{id}", response_description="Product data deleted from the database")
async def delete_product_data(id: str):
    deleted_product = await delete_product(id)
    if deleted_product:
        return ResponseModel(
            "Product with ID: {} removed".format(id), "Product deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Product with id {0} doesn't exist".format(id)
    )
