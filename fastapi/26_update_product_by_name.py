from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI() 

class ProductUpdate(BaseModel):
    price:Optional[float] = Field(
        default=None,
        gt=0,
        description='New price (must be positive)'
    )
    stock:Optional[int] = Field(
        default=None,
        ge=0,
        description='New stock (must be zero or positive)'
    )
    
products = [
    {"name": "Laptop", "price": 1200, "stock": 4},
    {"name": "Mouse", "price": 25, "stock": 20},
    {"name": "Keyboard", "price": 75, "stock": 8},
    {"name": "Monitor", "price": 300, "stock": 3},
    {"name": "USB Cable", "price": 10, "stock": 50}
]


@app.put("/products/{product_name}", status_code=status.HTTP_200_OK)

async def update_product(product_name: str, product_update: ProductUpdate):   
    for product in products:
        if product["name"] == product_name:
           if product_update.price is not None:
               product["price"] = product_update.price
           if product_update.stock is not None:
               product["stock"] = product_update.stock  
           return {
               "message": f"Product '{product_name}' updated successfully",
               "product": product
           }      
        
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail=f"Product '{product_name}' not found")