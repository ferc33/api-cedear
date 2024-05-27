from fastapi import FastAPI
from routers.stock import router as StockRouter

app = FastAPI()

app.include_router(StockRouter, prefix="/api", tags=["stocks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock API CEDEARS"}
