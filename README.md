# Python & FastAPI Practice

A collection of practical Python and FastAPI exercises covering data analysis, JSON handling, REST API development, request validation, and database integration.

This repository is part of my practical learning journey toward Python backend development and AI Agent development.

## Requirements

- Python 3.10+
- pip
- FastAPI
- Uvicorn
- SQLAlchemy

## Installation

Clone the repository:

```bash
git clone https://github.com/marykhodaparast/python_learning.git
cd python_learning
```

Install the required dependencies:

```bash
python3 -m pip install fastapi uvicorn sqlalchemy pydantic
```

Alternatively, use a specific Python interpreter:

```bash
/usr/bin/python3 -m pip install fastapi uvicorn sqlalchemy pydantic
```

## Running the FastAPI Application

The main FastAPI application is located in the `fastapi_project` directory.

First, navigate to the project directory:

```bash
cd fastapi_project
```

Start the development server:

```bash
python3 -m uvicorn main:app --reload
```

Alternatively, use a specific Python interpreter:

```bash
/usr/bin/python3 -m uvicorn main:app --reload
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
python3 -m uvicorn tamrin24:app --reload
```

General command format:

```bash
python3 -m uvicorn filename:app --reload
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
GET /products/UnknownProduct
```

The API should return a `404 Not Found` response.

## Database Integration

The project includes SQLAlchemy integration with SQLite.

- SQLAlchemy is used for database operations.
- SQLite stores application data locally.
- Database sessions are managed through a reusable dependency.
- Product endpoints are being migrated from in-memory storage to database-backed operations.

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
- HTTP Status Codes (200, 201, 204, 404, 409, 422)
- Interactive API documentation with Swagger UI

## Project Status

Python fundamentals and core FastAPI exercises have been implemented.

Database integration with SQLAlchemy is currently in progress.

**Next learning goals:**

- Complete database-backed CRUD operations
- Advanced FastAPI concepts
- External API integration
- LLM fundamentals and API integration
- AI Agents and tool calling
- LangGraph and MCP

