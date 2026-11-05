# Python & FastAPI Practice

A collection of practical Python and FastAPI exercises covering data analysis, JSON handling, REST API development, and request validation.

All exercises have been implemented and tested successfully.

## Requirements

- Python 3
- pip3
- FastAPI
- Uvicorn

## Installation

Install FastAPI and Uvicorn:

```bash
pip3 install fastapi uvicorn
```

Alternatively, install them using a specific Python interpreter:

```bash
/usr/bin/python3 -m pip install fastapi uvicorn
```

## Running the Application

Run the desired Python exercise using Uvicorn.

For example, if the file is named `tamrin24.py` and contains a FastAPI instance named `app`:

```bash
/usr/bin/python3 -m uvicorn tamrin24:app --reload
```

General command format:

cd fastapi_project

python3 -m uvicorn main:app --reload

```bash
python3 -m uvicorn filename:app --reload
```

Replace `filename` with the Python file name without the `.py` extension.

The `--reload` option automatically restarts the development server when code changes are detected.

Once the server starts, it is available at:

```text
http://127.0.0.1:8000
```

## Interactive API Documentation

FastAPI automatically generates interactive API documentation.

Open the following URL in your browser:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

You can use this page to explore endpoints and test API requests without installing additional tools.

## Testing API Endpoints

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
6. Check the response returned by the API.

### 2. Testing a POST Request

For example, to add a new transaction:

1. Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
2. Find the `POST /transactions` endpoint.
3. Click **Try it out**.
4. Enter the request body in JSON format:

```json
{
  "user": "Alex",
  "amount": 1500,
  "status": "success"
}
```

5. Click **Execute**.
6. Check the response body and HTTP status code.

A successful request should return a confirmation message, the newly added transaction, and the updated transaction count.

### 3. Testing Validation

The transaction endpoint also supports input validation through Pydantic.

Try sending invalid data, for example:

```json
{
  "user": "",
  "amount": -100,
  "status": "unknown"
}
```

FastAPI should reject the request and return a `422 Unprocessable Entity` response with validation details.

### 4. Testing a 404 Response

To test the product endpoint, try requesting a product that does not exist:

```text
GET /products/UnknownProduct
```

The API should return a `404 Not Found` response.

## Concepts Practiced

- Python functions and loops
- Lists and dictionaries
- Data analysis and aggregation
- JSON serialization and deserialization
- Reading and writing JSON files
- FastAPI application setup
- GET and POST HTTP methods
- Query Parameters
- Path Parameters
- HTTPException and error handling
- Pydantic models
- Data validation using Field and Literal
- Interactive API documentation with Swagger UI
- Response Models
- PUT and DELETE HTTP Methods
- HTTP Status Codes (200, 201, 404, 204)
- Partial Resource Updates
- CRUD Operations

## Project Status

All exercises have been implemented and tested successfully.

This repository is part of my practical learning journey toward Python backend development and AI Agent development.

**Next learning goals:** Advanced FastAPI concepts, API integration, LLMs, and AI Agents.