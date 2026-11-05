from pydantic import BaseModel, Field
from typing import Optional, Literal


class TransactionCreate(BaseModel):
    user: str = Field(
        min_length=1,
        max_length=50,
        description="Name of the user"
    )
    amount: int = Field(
        gt=0,
        description="Transaction amount (must be positive)"
    )
    status: Literal["success", "failed", "pending"] = Field(
        default=...,
        description="Transaction status"
    )


class TransactionResponse(BaseModel):
    user: str
    amount: int
    status: Literal["success", "failed", "pending"]