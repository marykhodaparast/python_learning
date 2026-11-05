from pydantic import BaseModel, Field

class CustomerCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    purchases: int = Field(gt=0)

class CustomerResponse(BaseModel):
    name: str
    purchases: int