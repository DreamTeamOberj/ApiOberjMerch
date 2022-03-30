from django.forms import BaseModelForm


class Product(BaseModelForm):
    
    name: str
    price: float
    description: str
    img: str
    
    # is_offer: Optional[bool] = None