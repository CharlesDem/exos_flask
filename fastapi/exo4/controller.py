from fastapi import APIRouter, Depends
from exo5.generic_response import ApiResponse
from exo4.model import OrderResponse
from .service import OrderService, get_order_service

exo4_router = APIRouter()


@exo4_router.post("/orders", response_model = ApiResponse[OrderResponse])
def create_order(payload: dict, service: OrderService = Depends(get_order_service)):
    order = service.create_order(payload)
    return ApiResponse(
        success = True,
        data = order, #pas clair
        message = f"total : {order.total}"
    )