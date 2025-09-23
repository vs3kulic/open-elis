from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session
from datetime import date
from data.models import SessionLocal
from data.models import Therapist

app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Therapist Database API!"}

@app.get("/therapists")
def get_therapists(limit: int = Query(10), offset: int = Query(0), district: str = Query(None),
                   method: str = Query(None), min_experience: int = Query(None), db: Session = Depends(get_db)):
    # Base query
    query = db.query(Therapist)

    # Apply filters if provided
    if district:
        query = query.filter(Therapist.postal_code == district)
    if method:
        query = query.filter(Therapist.therapy_methods == method)
    if min_experience:
        min_experience_date = date.today().replace(year=date.today().year - min_experience)
        query = query.filter(Therapist.registration_date <= min_experience_date)

    # Apply pagination
    therapists = query.offset(offset).limit(limit).all()
    return therapists
