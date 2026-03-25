from fastapi import FastAPI
from router import CustomRouter

app = FastAPI()

db = {}
router = CustomRouter(db)
app.include_router(router.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)

