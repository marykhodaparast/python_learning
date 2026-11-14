from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from schemas.product import ProductCreate, ProductUpdate, ProductResponse
from database import get_db
from models.product import Product


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

DbSession = Annotated[Session, Depends(get_db)]

@router.get(
    "/",
    response_model=list[ProductResponse],
    status_code=status.HTTP_200_OK
)
def get_products(
    db: DbSession,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(gt=0, le=100)] = 10
):
    products = db.scalars(
        select(Product)
        .order_by(Product.id)
        .offset(skip)
        .limit(limit)
    ).all()

    return products


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    status_code=status.HTTP_200_OK
)
def get_product(product_id: int, db: DbSession):
    # Find product using SQLAlchemy
    existing_product = db.scalar(
        select(Product).where(Product.id == product_id)
    )

    # Check if product exists
    if existing_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id '{product_id}' not found"
        )

    return existing_product


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(product: ProductCreate, db: DbSession):
    new_product = Product(**product.model_dump())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.patch(
    "/{product_id}",
    response_model=ProductResponse,
    status_code=status.HTTP_200_OK
)
def update_product(
    product_id: int,
    product_update: ProductUpdate,
    db: DbSession
):
    product = db.scalar(
        select(Product).where(Product.id == product_id)
    )

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id '{product_id}' not found"
        )

    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_product(product_id: int, db: DbSession):
    # Find the product
    existing_product = db.scalar(
        select(Product).where(Product.id == product_id)
    )

    # Check if product exists
    if existing_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id '{product_id}' not found"
        )

    # Delete the product
    db.delete(existing_product)
    db.commit()

    return None
