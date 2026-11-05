from fastapi import APIRouter, status
from schemas.transaction import TransactionCreate,TransactionResponse
from data import transactions

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/", response_model=list[TransactionResponse])
async def get_transactions():
    return transactions

@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction: TransactionCreate):
    new_transaction = transaction.model_dump()
    transactions.append(new_transaction)
    return new_transaction