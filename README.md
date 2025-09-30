# ELIS - Therapist Matching API

A FastAPI-based backend service for matching users with therapists based on questionnaire responses and filtering criteria.

## Project Structure

```
elis/
├── app/
│   ├── main.py                 # FastAPI app initialisation and router registration
│   ├── endpoints/              # API endpoint modules
│   │   ├── therapists.py       # Therapist listing and filtering
│   │   ├── therapy_types.py    # Therapy type endpoints
│   │   ├── therapy_methods.py  # Therapy method endpoints
│   │   ├── therapy_clusters.py # Therapy cluster endpoints
│   │   ├── calculate_result.py # Questionnaire processing
│   │   └── root.py            # Root endpoint
│   ├── utils/                 # Utility modules
│   │   ├── auth.py           # API key validation
│   │   ├── db.py             # Database session management
│   │   ├── middleware.py     # CORS and other middleware
│   │   └── api_key_generator.py # API key generation
│   └── calculate_cluster.py   # Questionnaire scoring logic
├── data/
│   ├── models.py             # SQLAlchemy database models
│   └── SessionLocal.py       # Database session configuration
├── logs/
│   └── worklog.md           # Development log
└── tests/                   # Test files
```

## Features

- RESTful API for therapist data management
- Questionnaire-based therapy cluster recommendation
- Filtering and pagination for all endpoints
- API key authentication
- CORS support for frontend integration

## API Endpoints

### Authentication
All endpoints require an `X-API-Key` header for authentication.

### Available Endpoints
- `GET /` - API status and welcome message
- `GET /therapists` - List therapists with filtering options
- `GET /therapy_types` - List therapy types
- `GET /therapy_methods` - List therapy methods
- `GET /therapy_clusters` - List therapy clusters
- `POST /calculate_result` - Process questionnaire responses

### Query Parameters
Most GET endpoints support:
- `limit` - Number of results to return (default: 10)
- `offset` - Number of results to skip (pagination)
- `cluster_short` - Filter by therapy cluster

Additional filters vary by endpoint (e.g., `postal_code`, `min_experience` for therapists).

## Setup

### Prerequisites
- Python 3.11+
- SQLite database with therapist data

### Installation
1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy python-dotenv
   ```
4. Create a `.env` file:
   ```
   API_KEY=your_generated_api_key
   ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
   ```

### Running the Server
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
