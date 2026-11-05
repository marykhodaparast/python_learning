from pydantic import BaseModel, Field
from typing import Optional


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="Product name")
    price: float = Field(gt=0, description="Price (must be positive)")
    stock: int = Field(ge=0, description="Stock (zero or positive)")


class ProductUpdate(BaseModel):
    price: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)


class ProductResponse(BaseModel):
    name: str
    price: float
    stock: int