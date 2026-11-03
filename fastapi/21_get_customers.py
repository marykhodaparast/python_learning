from fastapi import FastAPI

app = FastAPI()

customers = [
    {"name": "Ali", "purchases": 1200},
    {"name": "Sara", "purchases": 500},
    {"name": "John", "purchases": 2500},
    {"name": "Mary", "purchases": 1800},
    {"name": "David", "purchases": 700}
]

@app.get("/customers")

async def get_customers(min_purchase: int = 0):   
    filtered_customers = [
        customer for customer in customers
        if customer["purchases"] >= min_purchase
    ]
    return filtered_customers
    