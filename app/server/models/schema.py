import strawberry
from typing import Optional
from database import delete_product
from database import update_product
from database import add_product

from database import retrieve_products

@strawberry.type
class Product:
    id: Optional[str]
    name: Optional[str]
    price: Optional[float]
    description: Optional[str]
    is_offer: Optional[bool]
    
    
@strawberry.type
class Query:
    @strawberry.field
    async def products(self) -> list[Product]:
        dict_products = await retrieve_products()
        list_products = []
        for product in dict_products:
            list_products.append(Product(product['id'], product['name'], product['price'], product['description'], product['is_offer']))
        return list_products
        
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_product(self, name: str, price: float, description: str, is_offer: bool) -> str:
            await add_product({'name': name, 'price': price, 'description': description, 'is_offer': is_offer})
            return("Added product " + name)
        
    @strawberry.mutation
    async def update_product(self, id: str, name: str, price: float, description: str, is_offer: bool) -> str:
            await update_product(id, {'name': name, 'price': price, 'description': description, 'is_offer': is_offer})
            return("Updated product with id " + id)
        
    @strawberry.mutation
    async def delete_product(self, id: str) -> str:
            await delete_product(id)
            return("Deleted product with id " + id)
        
    @strawberry.mutation
    async def oberj(self) -> str:
            return("Oberj was here...")

    
    