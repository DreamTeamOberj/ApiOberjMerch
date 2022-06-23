import strawberry

from database import retrieve_products

@strawberry.type
class Product:
    name: str
    price: float
    description: str
    is_offer: bool
    
    
@strawberry.type
class Query:
    @strawberry.field
    def products(self) -> list[Product]:
        return retrieve_products()
        
    
    