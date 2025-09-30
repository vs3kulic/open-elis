"""This module provides a dependency to validate API keys for securing FastAPI endpoints."""
import os
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv

# Load environment variables from .env file, retrieve API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Define the API key header
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

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
    return None
