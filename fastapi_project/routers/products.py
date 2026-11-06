from fastapi import APIRouter, HTTPException, status, Depends
from schemas.product import ProductCreate, ProductUpdate, ProductResponse
from data import products

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
async def get_products(storage=Depends(get_product_storage)):
    return storage


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
async def create_product(product: ProductCreate, storage=Depends(get_product_storage)):
    if any(p["name"] == product.name for p in storage):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Product '{product.name}' already exists"
        )
    new_product = product.model_dump()
    storage.append(new_product)
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