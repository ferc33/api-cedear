from fastapi import APIRouter, HTTPException
from typing import List
from models.stock import Stock
from services.stock_service import get_top_gainers, get_top_losers

router = APIRouter()

@router.get("/stocks/gainers", response_model=List[Stock])
async def get_gainers():
    stocks = await get_top_gainers()
    if stocks:
        return stocks
    raise HTTPException(status_code=404, detail="No stocks found")

@router.get("/stocks/losers", response_model=List[Stock])
async def get_losers():
    stocks = await get_top_losers()
    if stocks:
        return stocks
    raise HTTPException(status_code=404, detail="No stocks found")
