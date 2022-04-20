import uuid
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserSchema(BaseModel):
    id: uuid.uuid4().int
    name: str
    first_name: str
    email: EmailStr
    password: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id":"0001" ,
                "name": "gab",
                "first_name": "ou",
                "email": "gabou@email.fr",
                "password": "0987653426",
            }
        }


class UpdateUserModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    first_name: Optional[float]
    email: Optional[str]
    password: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "id":"0001" ,
                "name": "gab",
                "first_name": "ou",
                "email": "gabou@email.fr",
                "password": "0987653426",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
