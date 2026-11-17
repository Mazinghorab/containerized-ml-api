<div align="center">

# ML API Service

A robust, production-ready RESTful API for serving Ride Deuration Machine Learning Model with high performance, scalability, and ease of use.

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-005571?logo=fastapi)](https://fastapi.tiangolo.com/)

</div>

---

## Overview

This repository provides a scalable backend service designed to serve machine learning predictions efficiently. Built with **FastAPI**, it offers automatic interactive documentation, robust input validation using **Pydantic**.

---

## Key Features

- **High Performance:** Built on **FastAPI** for asynchronous request handling and fast inference response times.
- **Input Validation:** Strict schema validation powered by **Pydantic** models to ensure robust data payloads.
- **Interactive Docs:** Auto-generated Swagger UI (`/docs`) and ReDoc (`/redoc`) endpoints for effortless testing.
- **Scalable Architecture:** Clean separation of concerns between API routing, and model loading.

---

## Project Structure

```text
ml-api/
├── src/
│   └── ml_api/
│       ├── Model/
│       │   └── predictor.py   # ML model loading and inference logic
│       ├── api/
│       │   ├── app.py         # FastAPI application setup and route definitions
│       │   └── schemas.py     # Pydantic data models for request/response validation
│       └── __init__.py
├── tests/                     # Unit and integration test suite
├── .gitignore                 # Git ignore rules
├── .python-version            # Pinned Python version for environment consistency
├── README.md                  # Project documentation
├── main.py                    # Application entrypoint
├── pyproject.toml             # Project metadata and dependencies
└── uv.lock                    # Exact dependency lockfile managed by uv
```

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your local machine:

* **Python** (matching the version specified in `.python-version`)
* **[uv](https://github.com/astral-sh/uv)** (recommended for fast package management)

### 1. Clone the Repository

```bash
git clone https://github.com/Mazinghorab/ml-api.git
cd ml-api
```

### 2. Install Dependencies

#### Option A: Using `uv` (Recommended)

`uv` will automatically create a virtual environment and install exact versions from `uv.lock`:

```bash
uv sync
```

#### Option B: Using Standard `venv` & `pip`

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -e .
```

### 3. Run the Application Locally

You can start the application using the `main.py` entrypoint or directly via Uvicorn:

```bash
# Using uv to run the entrypoint
uv run python main.py
```

Once running, open your browser and navigate to:

* **Swagger UI:** <http://localhost:8000/docs>
* **ReDoc:** <http://localhost:8000/redoc>

## API Endpoints

### 1. Health Check

* **Endpoint:** `GET /health` (or `GET /`)
* **Description:** Verifies that the API service and predictor are operational.
* **Response Example:**

  ```json
  {
    "status": "healthy"
  }
  ```

### 2. Prediction Endpoint

* **Endpoint:** `POST /predict`
* **Description:** Validates input features against `schemas.py` and runs inference via `predictor.py`.
* **Request Body Example:**

  ```json
  {
    "features": [100.0, 1]
  }
  ```

* **Response Example:**

  ```json
  {
    "probability": 10.0
  }
  ```

## Running Tests

Run the test suite located in the `tests/` directory using `pytest`:

```bash
uv run pytest
```
