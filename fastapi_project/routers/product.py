from fastapi import APIRouter, Depends
from schemas.customer import CustomerResponse
from fastapi_project.database import customers

router = APIRouter(prefix="/customers", tags=["Customers"])

def get_customer_storage():
    return customers

@router.get("/", response_model=list[CustomerResponse])
async def get_customers(min_purchase: int = 0,  storage = Depends(get_customer_storage)):
    return [c for c in storage if c["purchases"] >= min_purchase]