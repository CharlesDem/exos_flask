
from exo1 import User, UserCreate
from fastapi import FastAPI, HTTPException

from exo2 import Password
from exo3 import Product

app = FastAPI()

current_id = 1

db = {}

@app.post("/users", response_model=User, status_code=201)
def create_user(user_in: UserCreate):
    global current_id

    user = User(id=current_id, **user_in.model_dump())

    db[current_id] = user
    current_id += 1

    return user

@app.post("/pass", status_code=200)
def check_pass(password: Password):
    
    return {"message": "success"}

@app.post("/produict", status_code=201)
def check_pass(password: Product):
    return {"message": "success"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)

