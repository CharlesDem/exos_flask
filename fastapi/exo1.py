import re

from pydantic import BaseModel, Field, ConfigDict, field_validator, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=150)
    is_active: bool = True

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str):
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.match(pattern, v):
            raise ValueError("email format is not good")
        return v


# Output (avec id non modifiable)
class User(UserCreate):
    model_config = ConfigDict(frozen=True)
    id: int