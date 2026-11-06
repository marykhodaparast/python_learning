from fastapi import FastAPI
from routers import products_router, customers_router, transactions_router
from routers.external import router as external_router


app = FastAPI(
    title="Store Report API",
    description="A practice project for learning FastAPI",
    version="1.0.0"
)

app.include_router(products_router)

app.include_router(customers_router)

app.include_router(transactions_router)

app.include_router(external_router)


@app.get("/")
async def root():
    return {"message": "Store Report API is running. Go to /docs"}