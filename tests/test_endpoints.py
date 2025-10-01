"""
Unit tests for Open ELIS API endpoints.

This module contains tests for various API endpoints including therapists,
therapy types, methods, and clusters.

Note: The test_client and auth_headers fixtures are provided by conftest.py
"""

def test_unauthorized_access(test_client):
    """Test accessing protected endpoint without API key."""
    response = test_client.get("/therapists")  # No headers
    assert response.status_code == 403  # Should be forbidden

def test_get_therapists(test_client, auth_headers):
    """Test the GET /therapists endpoint."""
    response = test_client.get("/therapists", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  # Check that the list is not empty

def test_get_therapy_clusters(test_client, auth_headers):
    """Test the GET /therapy_clusters endpoint."""
    # TODO: Implement this test
    pass

def test_get_therapy_methods(test_client, auth_headers):
    """Test the GET /therapy_methods endpoint."""
    # TODO: Implement this test
    pass

def test_get_therapy_types(test_client, auth_headers):
    """Test the GET /therapy_types endpoint."""
    response = test_client.get("/therapy_types", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  # Check that the list is not empty

def test_calculate_result(test_client, auth_headers):
    """Test the POST /calculate_result endpoint."""
    # TODO: Implement this test
    pass
