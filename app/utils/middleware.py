"""This module contains middleware utilities for the FastAPI app."""

import os
from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    """
    Adds CORS middleware to the FastAPI app.

    :param app: FastAPI app instance.
    :type app: FastAPI
    """
    # Load allowed origins from environment variables
    allow_origins = os.getenv("ALLOWED_ORIGINS", "http://127.0.0.1:8001,http://localhost:8001").split(",")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=False,  # Set to True only if you need cookies/auth headers
        allow_methods=["GET", "POST", "OPTIONS"],  # Only methods you actually use
        allow_headers=["Accept", "Content-Type", "X-API-Key"],  # Your specific headers
    )
