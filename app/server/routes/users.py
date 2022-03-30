from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

users = APIRouter()


@users.get("/users")
def read_all_users(product_id: int):
    return {"product_id": product_id}


@users.get("/users/{users_id}")
def read_users(users_id: int):
    return {"users_id": users_id}