import re

from pydantic import BaseModel, Field, field_validator, model_validator


class Password(BaseModel):
    password: str = Field(..., min_length=8)
    confirm_password: str

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str):
        if not re.search(r"[a-z]", v):
            raise ValueError("Must have a lowercase letter")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Must have an uppercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Must have a digit")
        if not re.search(r"[^\w\s]", v):
            raise ValueError("Must have a symbol")
        return v

    @model_validator(mode="after") #c'est un @AssertTrue(message = "Passwords do not match") dans hibernate
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("passwords is not match")
        return self