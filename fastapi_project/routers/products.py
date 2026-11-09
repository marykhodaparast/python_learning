from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select

from schemas.product import ProductCreate, ProductUpdate, ProductResponse
from database import get_db
from models.product import Product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


def get_product_storage():
    return products

def get_mock_product_storage():
    return [
        {"name": "TestProduct", "price": 100, "stock": 5}
    ]


@router.get("/", response_model=list[ProductResponse], status_code=status.HTTP_200_OK)
async def get_products(db=Depends(get_db)):
    products = db.scalars(select(Product)).all()
    return products


@router.get("/{product_name}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(product_name: str, storage=Depends(get_product_storage)):
    product = next((p for p in storage if p["name"] == product_name), None)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product '{product_name}' not found"
        )
    return product


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db=Depends(get_db)):
    existing_product = db.scalar(
        select(Product).where(Product.name == product.name)
    )

    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Product '{product.name}' already exists"
        )

    new_product = Product(**product.model_dump())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.patch("/{product_name}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def update_product(
    product_name: str,
    product_update: ProductUpdate,
    storage=Depends(get_product_storage)
):
    product = next((p for p in storage if p["name"] == product_name), None)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product '{product_name}' not found"
        )
    if product_update.price is not None:
        product["price"] = product_update.price
    if product_update.stock is not None:
        product["stock"] = product_update.stock
    return product


@router.delete("/{product_name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_name: str, storage=Depends(get_product_storage)):
    product = next((p for p in storage if p["name"] == product_name), None)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product '{product_name}' not found"
        )
    storage.remove(product)
    return None