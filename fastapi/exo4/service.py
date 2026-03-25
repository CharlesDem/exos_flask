from exo4.dao import Item, Order, get_db
from fastapi import Depends

class OrderService:
    def __init__(self, db):
        self.db = db

    def create_order(self, data: dict):
        order = Order(
            customer_email=data["customer_email"],
            total=data["total"],
        )

        for i in data["items"]:
            order.items.append(
                Item(
                    product_id=i["product_id"],
                    quantity=i["quantity"],
                    price=i["price"],
                )
            )

        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)

        return order
    
def get_order_service(db = Depends(get_db)):
    return OrderService(db)