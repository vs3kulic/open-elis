# Readme for Open ELIS v0.1

## Introduction
ELIS is a non-profit project aimed at lowering the barriers to mental health access. This repository contains the backend implementation of the ELIS API.

## Features
- Provides information about therapists, their methods, and locations.
- Supports filtering by geographical location, therapy method, and years of experience.

## Parameters
- **Geographical preference**: Filter therapists by district.
- **Therapist preferences**: Filter by years of experience.
- **Personal preferences**: Filter by therapy method.

## Technology Stack
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **SQLite**: Lightweight database for storing therapist data.
- **SQLAlchemy**: ORM for database interactions.

## Requirements
- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/vs3kulic/open-elis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd open-elis
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the FastAPI application:
   ```bash
   uvicorn app.main:app --reload
   ```
6. Access the API documentation:
   - OpenAPI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License
This project is licensed under the MIT License.
