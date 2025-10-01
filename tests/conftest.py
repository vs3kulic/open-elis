"""
Shared pytest configuration and fixtures for the Open ELIS API tests.

This module contains reusable test fixtures and configuration that can be used
across all test modules in the tests/ directory.
"""
import json
import os
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.main import app

# ------------------------------
# Environment Setup
# ------------------------------
load_dotenv()

# ------------------------------
# Fixtures
# ------------------------------

@pytest.fixture
def test_client():
    """
    Create a test client for the FastAPI app.
    
    Returns:
        TestClient: A FastAPI test client instance for making HTTP requests.
    """
    return TestClient(app)

@pytest.fixture
def auth_headers():
    """
    Provide authentication headers with API key from environment.
    
    Returns:
        dict: Headers dictionary containing the X-API-Key header.
        
    Raises:
        pytest.skip: If API_KEY environment variable is not set.
    """
    api_key = os.getenv("API_KEY")
    if not api_key:
        pytest.skip("API_KEY environment variable not set")
    return {"X-API-Key": api_key}

@pytest.fixture
def sample_questionnaire_payload():
    """Load the complete questionnaire payload from mock_request.json."""
    mock_file_path = os.path.join(os.path.dirname(__file__), "mock_request.json")
    with open(mock_file_path, "r", encoding="cp1252") as f:
        return json.load(f)
