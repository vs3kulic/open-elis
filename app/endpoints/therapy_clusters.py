"""This module contains the theapy_clusters endpoint for retrieving therapy clusters."""
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from data.models import TherapyMethodCluster
from app.utils.validate_api_key import validate_api_key
from app.utils.db import get_db

# ------------------------------
# Endpoint definition
# ------------------------------

router = APIRouter()

@router.get("/therapy_clusters")
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
