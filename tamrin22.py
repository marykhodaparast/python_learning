from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI() 
    

products = [
    {"name": "Laptop", "price": 1200, "stock": 4},
    {"name": "Mouse", "price": 25, "stock": 20},
    {"name": "Keyboard", "price": 75, "stock": 8},
    {"name": "Monitor", "price": 300, "stock": 3},
    {"name": "USB Cable", "price": 10, "stock": 50}
]


@app.get("/products/{product_name}")
async def get_product(product_name: str):   
    for product in products:
        if product["name"] == product_name:
            return product
        
    raise HTTPException(status_code=404,detail=f"Product '{product_name}' not found")