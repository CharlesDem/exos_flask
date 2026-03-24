from pydantic import BaseModel, Field, field_validator
from typing import Optional
from enum import Enum
import re



class Category(str, Enum):
    ELECTRONICS = "ELECTRONICS"
    CLOTHING = "CLOTHING"
    FOOD = "FOOD"
    OTHER = "OTHER"


class Supplier(BaseModel):
    name: str = Field(..., min_length=1)
    email: str
    phone: Optional[str] = None

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str):
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.match(pattern, v):
            raise ValueError("Invalid email format")
        return v

class Product(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., ge=0)
    category: Category
    stock: int = Field(..., ge=0)
    supplier: Supplier