from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_user,
    delete_user,
    retrieve_users,
    retrieve_users,
    update_user,
)
from app.server.models.UserModel import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
)


users = APIRouter()


@users.get("/users")
async def read_all_users(users_id: int):
    return {"users_id": users_id}


@users.get("/users/{users_id}")
async def read_users(users_id: int):
    return {"users_id": users_id}


@users.post("/users/")
async def create_user(users_id: int):
    return {"users_id": users_id}


@users.put("/users/{users_id}")
async def update_users(users_id: int):
    return {"users_id": users_id}


@users.patch("/users/{users_id}")
async def patch_users(users_id: int):
    return {"users_id": users_id}


@users.delete("/users/{users_id}")
async def delete_users(users_id: int):
    return {"users_id": users_id}
