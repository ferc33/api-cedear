import yfinance as yf
from typing import List
from models.stock import Stock
from database import stock_collection
from datetime import datetime

CEDAR_CODES = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]  # Agrega los códigos de las acciones que quieres seguir

async def fetch_stock_data():
    stock_data = []
    for code in CEDAR_CODES:
        stock = yf.Ticker(code)
        stock_info = stock.history(period="1d")  # Obtener datos del último día
        if not stock_info.empty:
            latest_data = stock_info.iloc[-1]
            stock_data.append({
                "code": code,
                "name": stock.info['shortName'],
                "price": latest_data['Close'],
                "movement": latest_data['Close'] - latest_data['Open'],
                "date": datetime.now()
            })
    return stock_data

async def save_stock_data(stocks: List[dict]):
    await stock_collection.insert_many(stocks)

async def get_top_gainers() -> List[Stock]:
    stocks = await fetch_stock_data()
    gainers = sorted(stocks, key=lambda x: x['movement'], reverse=True)[:10]
    await save_stock_data(gainers)  # Guardar los datos en la base de datos
    return [Stock(**stock) for stock in gainers]

async def get_top_losers() -> List[Stock]:
    stocks = await fetch_stock_data()
    losers = sorted(stocks, key=lambda x: x['movement'])[:10]
    await save_stock_data(losers)  # Guardar los datos en la base de datos
    return [Stock(**stock) for stock in losers]
