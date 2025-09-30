"""This module contains the FastAPI apps and endpoints for the therapist database."""
from datetime import date
import os
from fastapi import FastAPI, Query, Depends, HTTPException
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from data.models import SessionLocal
from data.models import Therapist, TherapistAddress, TherapyMethod, TherapyMethodCluster, TherapyType
from app.calculate_cluster import process_all_responses, calculate_cluster

# ------------------------------
# API and Database Setup
# ------------------------------

# Load environment variables from .env file, retrieve API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Define the API key header
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Create FastAPI app instance
app = FastAPI()

# ------------------------------
# Dependencies and Middleware
# ------------------------------

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to validate the API key
def validate_api_key(api_key: str = Depends(api_key_header)):
    """
    Validate the provided API key against the expected value.
    
    :param api_key: The API key provided in the request header.
    :type api_key: str
    :raises HTTPException: If the API key is invalid.
    :return: None
    """
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8001", "http://localhost:8001"], # add PROD when ready
    allow_credentials=False,  # Set to True only if you need cookies/auth headers
    allow_methods=["GET", "POST", "OPTIONS"],  # Only methods you actually use
    allow_headers=[
        "Accept",
        "Content-Type", 
        "X-API-Key",  # Your specific API key header
    ],
)

# ------------------------------
# API Endpoints
# ------------------------------

@app.get("/")
def read_root():
    """
    Root endpoint to verify the API is running.
    
    :param: None
    :return: A welcome message.
    :rtype: dict
    """
    return {"message": "Welcome to the Therapist Database API!"}

@app.get("/therapists")
def get_therapists(
    _api_key: str = Depends(validate_api_key), # unused argument
    db: Session = Depends(get_db),
    limit: int = Query(10),
    offset: int = Query(0),
    min_experience: int = Query(None),
    therapy_method: str = Query(None),
    postal_code: str = Query(None),
    cluster_short: str = Query(None)
):
    """
    Retrieve a list of therapists with optional filtering.
    
    :param api_key: API key for authentication (validated).
    :param limit: Maximum number of results to return (default is 10).
    :param offset: Number of results to skip for pagination (default is 0).
    :param min_experience: Minimum years of experience required.
    :param therapy_method: Filter by specific therapy method.
    :param postal_code: Filter by postal code.
    :param db: Database session dependency.
    :return: List of therapists matching the criteria.
    :rtype: List[Therapist]
    """
    # Base query
    query = db.query(Therapist)

    # Filter by experience, postal code or therapy method
    if min_experience:
        min_experience_date = date.today().replace(year=date.today().year - min_experience)
        query = query.filter(Therapist.registration_date <= min_experience_date)
    if postal_code:
        query = query.join(
            TherapistAddress
            ).filter(
                TherapistAddress.postal_code == postal_code
            )
    if therapy_method:
        query = query.join(
            TherapyMethod, Therapist.therapy_methods
            ).filter(
                TherapyMethod.method_name == therapy_method
            )
    if cluster_short:
        query = query.join(
            TherapyMethod, Therapist.therapy_methods
        ).join(
            TherapyMethod.therapy_cluster
        ).filter(
            TherapyMethodCluster.cluster_short == cluster_short
        )

    # Apply pagination
    therapists = query.offset(offset).limit(limit).all()
    return therapists

@app.get("/therapy_methods")
def get_therapy_methods(
    _api_key: str = Depends(validate_api_key), # unused argument
    db: Session = Depends(get_db),
    limit: int = Query(25),
    offset: int = Query(0),
    method_name: str = Query(None),
    cluster_short: str = Query(None),
):
    """
    Retrieve a list of therapy methods with optional filtering.
    
    :param api_key: API key for authentication (validated).
    :param limit: Maximum number of results to return (default is 25).
    :param offset: Number of results to skip for pagination (default is 0).
    :param method_name: Filter by specific therapy method name.
    :param cluster_short: Filter by therapy cluster short code.
    :param db: Database session dependency.
    :return: List of therapy methods matching the criteria.
    :rtype: List[TherapyMethod]
    """
    # Base query
    query = db.query(TherapyMethod)

    # Filter by method name or therapy cluster
    if method_name:
        query = query.filter(TherapyMethod.method_name == method_name)
    if cluster_short:
        query = query.join(
            TherapyMethod.therapy_cluster).filter(
                TherapyMethodCluster.cluster_short == cluster_short
        )

    # Apply pagination
    therapy_methods = query.offset(offset).limit(limit).all()
    return therapy_methods

@app.get("/therapy_clusters")
def get_therapy_clusters(
    _api_key: str = Depends(validate_api_key), # unused argument
    db: Session = Depends(get_db),
    limit: int = Query(10),
    offset: int = Query(0),
    cluster_short: str = Query(None)
):
    """
    Retrieve a list of therapy method clusters with optional filtering.
    
    :param api_key: API key for authentication (validated).
    :param limit: Maximum number of results to return (default is 10).
    :param offset: Number of results to skip for pagination (default is 0).
    :param cluster_short: Filter by therapy cluster short code.
    :param db: Database session dependency.
    :return: List of therapy method clusters matching the criteria.
    :rtype: List[TherapyMethodCluster]
    """
    # Base query
    query = db.query(TherapyMethodCluster)

    # Filter by cluster short code
    if cluster_short:
        query = query.filter(TherapyMethodCluster.cluster_short == cluster_short)

    # Apply pagination
    clusters = query.offset(offset).limit(limit).all()
    return clusters

@app.get("/therapy_types")
def get_therapy_types(
    _api_key: str = Depends(validate_api_key), # unused argument
    db: Session = Depends(get_db),
    limit: int = Query(10),
    offset: int = Query(0),
    cluster_short: str = Query(None)
):
    """
    Retrieve a list of therapy types with optional filtering.
    
    :param api_key: API key for authentication (validated).
    :param db: Database session dependency.
    :param limit: Maximum number of results to return (default is 10).
    :param offset: Number of results to skip for pagination (default is 0).
    :param cluster_short: Filter by therapy cluster short code.
    :return: List of therapy types matching the criteria.
    :rtype: List[TherapyType]
    """
    # Base query
    query = db.query(TherapyType)

    # Filter by cluster short code
    if cluster_short:
        query = query.join(
            TherapyType.therapy_cluster).filter(
                TherapyMethodCluster.cluster_short == cluster_short
        )

    # Apply pagination
    clusters = query.offset(offset).limit(limit).all()
    return clusters

@app.post("/calculate_result")
def calculate_result(
    payload: dict,
    _api_key: str = Depends(validate_api_key)
):
    """
    Calculate the recommended therapy cluster based on questionnaire responses.

    :param api_key: API key for authentication (validated).
    :param payload: JSON payload containing questionnaire responses.
    :type payload: dict
    :return: Recommended therapy cluster.
    :rtype: dict
    """
    responses = payload.get("responses", [])
    if not responses:
        return {"error": "No responses provided"}, 400

    # Process responses, calculate scores, and determine best cluster
    scores = process_all_responses(responses)
    best_cluster = calculate_cluster(scores)

    return {"recommended_cluster": best_cluster}
