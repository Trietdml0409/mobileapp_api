from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    image: str
    createdAt: str
    isBestSeller: bool
    brandName: str
    liked: bool = False

class Username(BaseModel):
    id: int
    username: str
    password: str
    createdAt: str



