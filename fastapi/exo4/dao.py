from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from uuid import uuid4
from .db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    customer_email = Column(String)
    total = Column(Float)
    items = relationship("Item")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    quantity = Column(Integer)
    price = Column(Float)

    order_id = Column(String, ForeignKey("orders.order_id"))