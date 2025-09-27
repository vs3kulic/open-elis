from datetime import date
from fastapi import FastAPI, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from data.models import SessionLocal
from data.models import Therapist, TherapistAddress, TherapyMethod, TherapyMethodCluster

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8001", "http://localhost:8001"], # add PROD when ready
    allow_credentials=False,  # Set to True only if you need cookies/auth headers
    allow_methods=["GET", "POST", "OPTIONS"],  # Only methods you actually use
    allow_headers=[
        "Accept",
        "Content-Type", 
        "X-API-Key",  # Your specific API key header
    ],
)

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
def get_therapists(
    limit: int = Query(10),
    offset: int = Query(0),
    min_experience: int = Query(None),
    therapy_method: str = Query(None),
    postal_code: str = Query(None),
    db: Session = Depends(get_db)
):
    # Base query
    query = db.query(Therapist)

    # Filter by therapist experience, postal code (join with TherapistAddress) or therapy method (join with TherapyMethod)
    if min_experience:
        min_experience_date = date.today().replace(year=date.today().year - min_experience)
        query = query.filter(Therapist.registration_date <= min_experience_date)
    if postal_code:
        query = query.join(TherapistAddress).filter(TherapistAddress.postal_code == postal_code)
    if therapy_method:
        query = query.join(TherapyMethod, Therapist.therapy_methods).filter(TherapyMethod.method_name == therapy_method)

    # Apply pagination
    therapists = query.offset(offset).limit(limit).all()
    return therapists

@app.get("/therapy_methods")
def get_therapy_methods(limit: int = Query(25), offset: int = Query(0), method_name: str = Query(None),
                   therapy_cluster: str = Query(None), db: Session = Depends(get_db)):

    # Base query
    query = db.query(TherapyMethod)

    if method_name:
        query = query.filter(TherapyMethod.method_name == method_name)
    if therapy_cluster:
        query = query.join(
            TherapyMethod.therapy_cluster).filter(
                TherapyMethodCluster.cluster_short == therapy_cluster
        )

    therapy_methods = query.offset(offset).limit(limit).all()
    return therapy_methods
