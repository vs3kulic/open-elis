"""This module contains the FastAPI apps and endpoints for the therapist database."""
from fastapi import FastAPI
from app.utils.middleware import add_cors_middleware
from app.endpoints.calculate_result import router as calculate_result_router
from app.endpoints.therapy_types import router as therapy_types_router
from app.endpoints.therapy_methods import router as therapy_methods_router
from app.endpoints.therapy_clusters import router as therapy_clusters_router
from app.endpoints.therapists import router as therapists_router
from app.endpoints.root import router as root_router

# ------------------------------
# App Setup
# ------------------------------

# Create FastAPI app instance
app = FastAPI(
    title="Open ELIS API",
    description="API for managing therapist data, therapy types, and clusters.",
    version="0.1.0",
)

# Add CORS middleware
add_cors_middleware(app)

# Register routers
app.include_router(calculate_result_router)
app.include_router(therapy_types_router)
app.include_router(therapy_methods_router)
app.include_router(therapy_clusters_router)
app.include_router(root_router)
app.include_router(therapists_router)
