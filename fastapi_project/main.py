from fastapi import FastAPI
from database import Base, engine
from models.product import Product  
from routers.products import router as products_router
from routers.customers import router as customers_router
from routers.transactions import router as transactions_router


app = FastAPI(
    title="Store Report API",
    description="A practice project for learning FastAPI",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(products_router)
app.include_router(customers_router)
app.include_router(transactions_router)


@app.get("/")
async def root():
    return {"message": "Store Report API is running. Go to /docs"}