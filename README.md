# Open ELIS v0.1

## Introduction
**ELIS** (Easy Locator for Inclusive Support) is a non-profit project aimed at lowering barriers to mental health access. This repository contains the backend implementation of the ELIS API.

## Features
- Provides information about therapists, their methods, and locations.
- Supports filtering by:
  - **Geographical location** (districts).
  - **Therapy method** (e.g., CBT, psychoanalysis).
  - **Years of experience**.
- Recommends therapists based on user preferences and questionnaire results.

## Technology Stack
- **FastAPI**: A modern, high-performance web framework for building APIs with Python.
- **SQLite**: Lightweight database for storing therapist data.
- **SQLAlchemy**: ORM for database interactions.
- **Sphinx**: For generating API documentation.

## Requirements
- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite

## Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/vs3kulic/open-elis.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd open-elis
   ```
3. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the FastAPI application**:
   ```bash
   uvicorn app.main:app --reload
   ```
6. **Access the API documentation**:
   - OpenAPI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints
### `/calculate_result` (POST)
- **Description**: Processes questionnaire responses and calculates the best therapy cluster.
- **Request**: JSON payload with 26 responses.
- **Response**: Recommended therapy cluster (`cluster_short`).

### `/therapists` (GET)
- **Description**: Retrieves a list of therapists with optional filtering.
- **Query Parameters**:
  - `cluster_short`: Filter by therapy cluster.
  - `min_experience`: Minimum years of experience.
  - `postal_code`: Filter by postal code.
  - `therapy_method`: Filter by specific therapy method.

## License
This project is licensed under the MIT License.
