"""This module contains the therapy_methods endpoint for retrieving therapy methods."""
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from data.models import TherapyMethod, TherapyMethodCluster
from app.utils.validate_api_key import validate_api_key
from app.utils.db import get_db

# ------------------------------
# Endpoint definition
# ------------------------------

router = APIRouter()

@router.get("/therapy_methods")
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