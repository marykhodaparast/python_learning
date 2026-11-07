import pytest
from fastapi.testclient import TestClient
from main import app
import fastapi_project.database as database

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_products():
    database.products.clear()
    database.products.extend([
        {"name": "Laptop", "price": 1200, "stock": 4},
        {"name": "Mouse", "price": 25, "stock": 20},
    ])
    yield

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    
def test_create_product():
    new_product = {"name": "Tablet", "price": 500, "stock": 10}
    response = client.post("/products/", json=new_product)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Tablet"
    
def test_create_duplicate_product():
    product = {"name": "Laptop", "price": 1200, "stock": 4}  
    response = client.post("/products/", json=product)
    assert response.status_code == 409   
    
def test_get_nonexistent_product():
    response = client.get("/products/Phone")
    assert response.status_code == 404
    assert "detail" in response.json() 
    
def test_create_product_negative_price():
    bad_product = {"name": "Bad", "price": -10, "stock": 5}
    response = client.post("/products/", json=bad_product)
    assert response.status_code == 422
    
def test_delete_product():
    response = client.delete("/products/Mouse")
    assert response.status_code == 204
    assert response.content == b""

    response2 = client.get("/products/Mouse")
    assert response2.status_code == 404           