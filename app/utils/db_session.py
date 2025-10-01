"""This module contains the database session utility for FastAPI endpoints."""
from data.models import SessionLocal

# Dependency to get a database session
def get_db():
    """Yield a database session and ensure it's closed after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()