# Week 7 Day 1 PM: Python APIs with Flask and FastAPI

## Objective

Learn how to build REST APIs in Python using Flask and FastAPI, understand request handling and routing, and compare the strengths of both frameworks.

---

## Flask vs FastAPI

### Flask

Flask is a lightweight Python web framework commonly used for prototypes and simple APIs.

#### Advantages

- Simple and easy to learn
- Lightweight
- Flexible
- Quick API development

#### Disadvantages

- Manual input validation
- No automatic API documentation
- Additional libraries needed for advanced features

### FastAPI

FastAPI is a modern Python API framework that uses type hints and Pydantic for validation.

#### Advantages

- Automatic request validation
- Built-in Swagger documentation
- Strong type checking
- Better performance
- Native async support

#### Disadvantages

- Steeper learning curve
- Requires understanding Pydantic models

---

## Flask Transaction API

### Endpoints Implemented

#### GET /health

Returns API health status.

Example Response:

```json
{
    "status": "ok"
}
```

#### POST /transactions

Creates a new transaction.

Example Request:

```json
{
    "account_id": "ACC-001",
    "amount": 500.00,
    "currency": "ZAR"
}
```

Example Response:

```json
{
    "id": "uuid",
    "account_id": "ACC-001",
    "amount": 500.00,
    "currency": "ZAR",
    "status": "pending",
    "created_at": "2026-08-26T13:59:04"
}
```

#### GET /transactions

Returns all stored transactions.

---

## FastAPI Transaction API

### Features

- Automatic validation using Pydantic
- Swagger documentation
- Type annotations
- HTTP status codes
- Middleware support

### Endpoints Implemented

#### GET /health

Returns service health information.

#### POST /transactions

Creates a transaction with validation.

Validation includes:

- Account ID required
- Amount must be positive
- Currency must be a valid 3-letter ISO code

#### GET /transactions

Returns all transactions.

#### GET /transactions/{id}

Returns a single transaction by ID.

Returns:

- HTTP 200 if found
- HTTP 404 if not found

#### PATCH /transactions/{id}/status

Updates transaction status.

Allowed values:

```text
approved
rejected
```

Invalid values return HTTP 400.

---

## Middleware

### X-Request-ID Header

A middleware function generates a unique UUID for every request and attaches it to the response headers.

Purpose:

- Request tracing
- Auditability
- Troubleshooting
- Distributed system monitoring

---

## Testing Results

### Flask API

Successfully tested:

- GET /health
- POST /transactions

Results:

- HTTP 200 returned for health endpoint
- HTTP 201 returned for transaction creation
- UUID generated successfully
- Default status set to pending

Example transaction created:

```text
Account: ACC-001
Amount