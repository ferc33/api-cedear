from pydantic import BaseModel, Field

class Stock(BaseModel):
    code: str = Field(...)
    name: str = Field(...)
    price: float = Field(...)
    movement: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "code": "AAPL",
                "name": "Apple Inc.",
                "price": 150.0,
                "movement": 5.0,
            }
        }
