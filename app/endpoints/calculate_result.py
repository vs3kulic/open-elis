"""This module contains the calculate_result endpoint for processing questionnaire responses."""
from fastapi import APIRouter, Depends, HTTPException
from app.calculations.calculate_cluster import process_all_responses, calculate_cluster
from app.utils.validate_api_key import validate_api_key

# ------------------------------
# Endpoint definition
# ------------------------------

router = APIRouter()

@router.post("/calculate_results")
def calculate_results(
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
        raise HTTPException(status_code=400, detail="No responses provided")

    # Process responses, calculate scores, and determine best cluster
    scores = process_all_responses(responses)
    best_cluster = calculate_cluster(scores)

    return {"recommended_cluster": best_cluster}
