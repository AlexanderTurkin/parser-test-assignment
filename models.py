from pydantic import BaseModel
from typing import Union


class Manufacturer(BaseModel):
    name: str


class Price(BaseModel):
    price: Union[float, None]
    old_price: Union[float, None]


class Stocks(BaseModel):
    prices: Price


class Product(BaseModel):
    id: int
    name: str
    url: str
    stocks: list[Stocks]
    manufacturer: Manufacturer


class Products(BaseModel):
    products: list[Product]