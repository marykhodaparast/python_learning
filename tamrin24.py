from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Literal

app = FastAPI() 

class Transaction(BaseModel):
    user:str = Field(
        min_length=1,
        max_length=50,
        description="Name of the user"
    )
    amount:int = Field(
        gt=0,
        description="Transaction amount (must be positive)"
    )
    status: Literal["success", "failed", "pending"] = Field(
        description="Transaction status"
    )
     
transactions = [
    {"user": "Ali", "amount": 1200, "status": "success"},
    {"user": "Sara", "amount": 500, "status": "failed"},
    {"user": "John", "amount": 2500, "status": "success"},
    {"user": "Mary", "amount": 1800, "status": "success"},
    {"user": "David", "amount": 700, "status": "pending"},
    {"user": "Ali", "amount": 900, "status": "success"}
]

@app.post("/transactions")

async def post_transaction(transaction: Transaction):   
    new_transaction = transaction.model_dump()
    transactions.append(new_transaction)
    
    return {
        "message": "Transaction added successfully",
        "transaction": new_transaction,
        "total_transactions": len(transactions)
    }
    
        