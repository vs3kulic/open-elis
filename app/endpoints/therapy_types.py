"""This module contains the therapy_types endpoint for retrieving therapy types."""
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from data.models import TherapyType, TherapyMethodCluster
from app.utils.validate_api_key import validate_api_key
from app.utils.db_session import get_db

# ------------------------------
# Endpoint definition
# ------------------------------

router = APIRouter()

@router.get("/therapy_types")
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
