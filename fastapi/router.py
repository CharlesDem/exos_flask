from fastapi import APIRouter
from exo1 import User, UserCreate
from exo2 import Password
from exo3 import Product


class CustomRouter:

    def __init__(self, db): #db devrait être un service à injecter plutôt
        self.db = db
        self.__router = APIRouter(prefix="/fastapi")
        self.current_id = 1

        self.__router.post("/users", response_model=User, status_code=201)(self.create_user)
        self.__router.post("/produict", status_code=201)(self.create_product)
        self.__router.post("/pass", status_code=200)(self.check_pass)

    def create_user(self, user_in: UserCreate):     
        user = User(id=self.current_id, **user_in.model_dump())
        self.db[self.current_id] = user
        self.current_id += 1
        return user

    def check_pass(self, password: Password):
        return {"message": "success"}

    def create_product(self, password: Product):
        return {"message": "success"}
    
    @property
    def router(self):
        return self.__router