from fastapi import APIRouter, Depends
from .service import OrderService, get_order_service

exo4_router = APIRouter()


@exo4_router.post("/orders")
def create_order(payload: dict, service: OrderService = Depends(get_order_service)):
    return service.create_order(payload)