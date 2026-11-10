
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from database import Base, get_db
from models.product import Product


# Create a separate in-memory database for tests
SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


@pytest.fixture(autouse=True)
def setup_test_database():
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    yield

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


client = TestClient(app)


def test_get_products():
    response = client.get("/products/")

    assert response.status_code == 200
    assert response.json() == []
    
def test_create_product():
    new_product = {
        "name": "Tablet",
        "price": 500,
        "stock": 10
    }

    response = client.post("/products/", json=new_product)

    assert response.status_code == 201

    data = response.json()

    assert data["id"] is not None
    assert data["name"] == "Tablet"
    assert data["price"] == 500
    assert data["stock"] == 10    
    

def test_create_duplicate_product():
    first_product = {
        "name": "Laptop",
        "price": 1200,
        "stock": 4
    }

    second_product = {
        "name": "Laptop",
        "price": 2340,
        "stock": 50
    }

    first_response = client.post("/products/", json=first_product)
    second_response = client.post("/products/", json=second_product)

    assert first_response.status_code == 201
    assert second_response.status_code == 201

    assert first_response.json()["id"] != second_response.json()["id"]
    
def test_get_product_by_id():
    new_product = {
        "name": "Keyboard",
        "price": 80,
        "stock": 15
    }

    create_response = client.post("/products/", json=new_product)
    product_id = create_response.json()["id"]

    response = client.get(f"/products/{product_id}")

    assert response.status_code == 200
    assert response.json()["id"] == product_id
    assert response.json()["name"] == "Keyboard"
    assert response.json()["price"] == 80
    assert response.json()["stock"] == 15   
    
def test_get_nonexistent_product():
    response = client.get("/products/99999")

    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()  
    
def test_update_product():
    new_product = {
        "name": "Monitor",
        "price": 300,
        "stock": 8
    }

    create_response = client.post("/products/", json=new_product)
    product_id = create_response.json()["id"]

    update_response = client.patch(
        f"/products/{product_id}",
        json={"price": 450}
    )

    assert update_response.status_code == 200

    data = update_response.json()

    assert data["id"] == product_id
    assert data["price"] == 450
    assert data["stock"] == 8       
    
def test_delete_product():
    new_product = {
        "name": "Mouse",
        "price": 25,
        "stock": 20
    }

    create_response = client.post("/products/", json=new_product)
    product_id = create_response.json()["id"]

    delete_response = client.delete(f"/products/{product_id}")

    assert delete_response.status_code == 204
    assert delete_response.content == b""

    get_response = client.get(f"/products/{product_id}")

    assert get_response.status_code == 404    
    
def test_create_product_with_negative_price():
    new_product = {
        "name": "Invalid Product",
        "price": -100,
        "stock": 5
    }

    response = client.post("/products/", json=new_product)

    assert response.status_code == 422    
    

