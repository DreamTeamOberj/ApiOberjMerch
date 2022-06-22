from pydantic import BaseModel
from typing import Optional


class ProductSchema(BaseModel):
    name: Optional[str]
    price: Optional[float]
    description: Optional[str]
    is_offer: Optional[bool]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "T-shirt bg",
                "price": 101,
                "description": "tshirt de bonne qualité",
                "is_offer": False,
            }
        }


class UpdateProductModel(BaseModel):
    name: Optional[str]
    price: Optional[float]
    description: Optional[str]
    is_offer: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "T-shirt bgggg",
                "price": 101,
                "description": "tshirt de bonen qualité",
                "is_offer": False,
            }
        }


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
