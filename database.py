from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import DESCENDING

MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.stocks_db
stock_collection = database.get_collection("stocks")
