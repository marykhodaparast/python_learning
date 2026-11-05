from fastapi import APIRouter, HTTPException, status
from schemas.product import ProductCreate, ProductUpdate, ProductResponse
from data import products

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("", response_model=list[ProductResponse], status_code=status.HTTP_200_OK)
async def get_products():
    return products


@router.get("/{product_name}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(product_name: str):
    product = next((p for p in products if p["name"] == product_name), None)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product '{product_name}' not found"
        )
    return product


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    if any(p["name"] == product.name for p in products):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Product '{product.name}' already exists"
        )
    new_product = product.model_dump()
    products.append(new_product)
    return new_product


@router.patch("/{product_name}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def update_product(product_name: str, product_update: ProductUpdate):
    product = next((p for p in products if p["name"] == product_name), None)
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
async def delete_product(product_name: str):
    product = next((p for p in products if p["name"] == product_name), None)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product '{product_name}' not found"
        )
    products.remove(product)
    return None