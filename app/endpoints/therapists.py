"""This module contains the therapists endpoint for retrieving therapists."""
from datetime import date
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from data.models import Therapist, TherapistAddress, TherapyMethod, TherapyMethodCluster
from app.utils.validate_api_key import validate_api_key
from app.utils.db import get_db


# ------------------------------
# Endpoint definition
# ------------------------------

router = APIRouter()

@router.get("/therapists")
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
