# routers/customers.py
from fastapi import APIRouter
from schemas.customer import CustomerResponse
from data import customers

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/", response_model=list[CustomerResponse])
async def get_customers(min_purchase: int = 0):
    return [c for c in customers if c["purchases"] >= min_purchase]