from pydantic import BaseModel
from typing import Generic, TypeVar, Optional
from datetime import datetime

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]): #utilisé dans l'exo4
    success: bool
    data: Optional[T]
    message: str
    timestamp: str = datetime.now().isoformat()