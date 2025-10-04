from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    """
    Root endpoint to verify the API is running.

    :param: None
    :return: A welcome message.
    :rtype: dict
    """
    return {"message": "Welcome to the ELIS API! Your gateway to personalised therapy recommendations."}