from fastapi import FastAPI,status,Query
from pydantic import BaseModel,Field

app = FastAPI()

class Customer(BaseModel):
    name:str = Field(
        min_length=3,
        max_length=50,
        description="Name of the user"
    )
    purchases:int = Field(
        gt=0,
        description="Purchase amount (must be positive)"
    )

class CustomerResponse(BaseModel):
    name: str
    purchases: int       

customers = [
    {"name": "Ali", "purchases": 1200},
    {"name": "Sara", "purchases": 500},
    {"name": "John", "purchases": 2500},
    {"name": "Mary", "purchases": 1800},
    {"name": "David", "purchases": 700}
]

@app.get("/customers", response_model = list[CustomerResponse], status_code=status.HTTP_200_OK)

async def get_customers(min_purchase: int = Query(default=0, ge=0)):   
    filtered_customers = [
        customer for customer in customers
        if customer["purchases"] >= min_purchase
    ]
    return filtered_customers
    