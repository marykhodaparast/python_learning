from fastapi import FastAPI,HTTPException,status

app = FastAPI() 
    
products = [
    {"name": "Laptop", "price": 1200, "stock": 4},
    {"name": "Mouse", "price": 25, "stock": 20},
    {"name": "Keyboard", "price": 75, "stock": 8},
    {"name": "Monitor", "price": 300, "stock": 3},
    {"name": "USB Cable", "price": 10, "stock": 50}
]


@app.delete("/products/{product_name}", status.HTTP_200_OK)

async def delete_product(product_name: str):   
    for product in products:
        if product["name"] == product_name:
           products.remove(product)
           
           return {
               "message": f"Product '{product_name}' deleted successfully",
               "deleted_product": product,
               "total_products": len(products)
           }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product '{product_name}' not found")