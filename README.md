# Python & FastAPI Practice

A collection of practical Python and FastAPI exercises covering data analysis, JSON handling, REST API development, request validation, and database integration.

This repository is part of my practical learning journey toward Python backend development and AI Agent development.

## Requirements

- Python 3.10+
- pip
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Pytest
- HTTPX

## Installation

Clone the repository:

```bash
git clone https://github.com/marykhodaparast/python_learning.git
cd python_learning
```

Navigate to the FastAPI project directory:

```bash
cd fastapi_project
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
python -m pip install fastapi uvicorn sqlalchemy pydantic pytest httpx
```

Using a virtual environment keeps project dependencies isolated from the system Python installation.

## Running the FastAPI Application

The main FastAPI application is located in the `fastapi_project` directory.

If you are not already there, navigate to it:

```bash
cd fastapi_project
```

Activate the virtual environment if it is not active:

```bash
source .venv/bin/activate
```

Start the development server:

```bash
python -m uvicorn main:app --reload
```

The `--reload` option automatically restarts the server whenever code changes are detected.

Once the server starts, open:

- API: http://127.0.0.1:8000
- Interactive API documentation: http://127.0.0.1:8000/docs
- Alternative API documentation: http://127.0.0.1:8000/redoc

## Running Individual Exercises

You can also run individual FastAPI exercises using Uvicorn.

For example, if `tamrin24.py` contains a FastAPI instance named `app`:

```bash
python -m uvicorn tamrin24:app --reload
```

General command format:

```bash
python -m uvicorn filename:app --reload
```

Replace `filename` with the Python file name without the `.py` extension.

## Testing API Endpoints

FastAPI automatically generates interactive API documentation.

Open:

http://127.0.0.1:8000/docs

You can explore and test API endpoints directly through Swagger UI.

### 1. Testing a GET Request

For example, to retrieve customers:

```text
GET /customers?min_purchase=1000
```

Steps:

1. Open `/docs`.
2. Find the `GET /customers` endpoint.
3. Click **Try it out**.
4. Enter a value for `min_purchase`, such as `1000`.
5. Click **Execute**.
6. Check the API response.

### 2. Testing a POST Request

For example, to add a new transaction:

```json
{
  "user": "Alex",
  "amount": 1500,
  "status": "success"
}
```

1. Find the `POST /transactions` endpoint.
2. Click **Try it out**.
3. Enter the JSON request body.
4. Click **Execute**.
5. Check the response body and HTTP status code.

### 3. Testing Validation

Try sending invalid data:

```json
{
  "user": "",
  "amount": -100,
  "status": "unknown"
}
```

FastAPI should reject invalid input and return a `422 Unprocessable Entity` response with validation details.

### 4. Testing a 404 Response

Try requesting a product that does not exist:

```text
GET /products/99999
```

The API should return a `404 Not Found` response.

## Database Integration

The project includes SQLAlchemy integration with SQLite.

- SQLAlchemy is used for database operations.
- SQLite stores application data locally.
- Database sessions are managed through a reusable dependency.
- Product CRUD endpoints are fully integrated with SQLite using SQLAlchemy.

The database file is created automatically when the application starts.

## Concepts Practiced

- Python functions and loops
- Lists and dictionaries
- Data analysis and aggregation
- JSON serialization and deserialization
- Reading and writing JSON files
- FastAPI application setup
- GET, POST, PATCH, and DELETE methods
- Query Parameters and Path Parameters
- HTTPException and error handling
- Pydantic models and data validation
- Field constraints and Literal types
- Response Models
- Dependency Injection
- SQLAlchemy ORM
- SQLite database integration
- Database sessions and CRUD operations
- SQLAlchemy Session type hints
- Generator type hints for database dependencies
- Database session lifecycle and cleanup with `yield`, `try/finally`, and `db.close()`
- Virtual environments with Python `venv`
- HTTP Status Codes (200, 201, 204, 404, 422)
- Interactive API documentation with Swagger UI
- API testing with Pytest and FastAPI TestClient

## Project Status

Python fundamentals and core FastAPI exercises have been implemented.

Database integration and Product CRUD operations are completed and tested.

### Product CRUD API Testing

Completed comprehensive API testing for the Product CRUD endpoints.

**Tests implemented:**

- Retrieve all products.
- Create a product and validate its response.
- Allow products with duplicate names.
- Retrieve a product by ID.
- Handle non-existent products with HTTP 404.
- Update product fields using PATCH.
- Preserve unchanged fields during partial updates.
- Delete products and verify successful deletion.
- Validate negative prices and reject invalid input with HTTP 422.
- Verify PATCH and DELETE behavior for non-existent products.
- Update product stock independently while preserving its price.
- Reject negative stock values with HTTP 422.

**Testing setup:**

- Pytest
- FastAPI TestClient
- In-memory SQLite database
- SQLAlchemy StaticPool
- FastAPI dependency overrides

**Latest test result:**

- Python 3.13.1
- 11 tests passed
- 1 deprecation warning from the Starlette TestClient / HTTPX integration

All 11 tests passed successfully.

### Advanced FastAPI: Dependency Injection and Database Sessions

Completed the following improvements and learning tasks:

- Added SQLAlchemy `Session` type hints to all Product CRUD endpoints.
- Added `Generator[Session, None, None]` as the return type hint for the `get_db` dependency.
- Reviewed how FastAPI provides dependencies through `Depends(get_db)`.
- Practiced database session lifecycle management using `yield` and `try/finally`.
- Ensured database sessions are closed with `db.close()` after use.
- Created and activated a project-specific virtual environment using `venv`.
- Installed dependencies inside the virtual environment.
- Verified the test suite using Python 3.13.1.

**Key concept:**

The `Session` type hint describes the expected type of the database object, while `Depends(get_db)` tells FastAPI how to provide that object to an endpoint.

**Status:** Completed.

**Next learning goals:**

- External API integration
- Further advanced FastAPI concepts
- LLM fundamentals and API integration
- AI Agents and tool calling
- LangGraph and MCP
- RAG, security, testing, and deployment
