"""This module contains the database session utility for FastAPI."""
from data.models import SessionLocal

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()