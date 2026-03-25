from fastapi import FastAPI
from exo4.controller import exo4_router
from exo4.dao import Base
from exo4.db import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

db = {}
# router = CustomRouter(db)
app.include_router(exo4_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)

