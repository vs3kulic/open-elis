from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Therapist(Base):
    __tablename__ = 'therapists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    title = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=False)
    registration_date = Column(Date, nullable=False)
    registration_number = Column(Integer, nullable=False, unique=True)
    state = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    therapy_methods = Column(String, nullable=False)

# Database setup
DATABASE_URL = "sqlite:///./therapists.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)
