from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, model_validator, EmailStr

class Item(BaseModel):
    product_id: int
    quantity: int = Field(..., ge=1)
    price: float = Field(..., gt=0)

class Commande(BaseModel):
    order_id: UUID = Field(default_factory=uuid4)
    customer_email: EmailStr
    items: List[Item] = Field(..., min_length=1)
    total: Optional[float] = None

    @model_validator(mode="after")
    def compute_or_validate_total(self):
        computed_total = sum(item.quantity * item.price for item in self.items)

        if self.total is None:
            self.total = computed_total
        else:
            if abs(self.total - computed_total) > 1e-6:
                raise ValueError("is not good number")

        return self