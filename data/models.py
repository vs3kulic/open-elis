from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Association table for many-to-many relationship
therapist_therapy_method = Table(
    'therapist_therapy_method',
    Base.metadata,
    Column('therapist_id', Integer, ForeignKey('therapists.id'), primary_key=True),
    Column('therapy_method_id', Integer, ForeignKey('therapy_methods.id'), primary_key=True)
)

class Therapist(Base):
    """Data model for therapists."""
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
    therapy_methods = relationship("TherapyMethod", secondary=therapist_therapy_method, back_populates="therapists")

class TherapyMethod(Base):
    """Data model for therapy methods, as indicated by source data."""
    __tablename__ = 'therapy_methods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    method_name = Column(String, nullable=False, unique=False)
    method_cluster = Column(String, nullable=True, unique=False)
    therapist_id = Column(Integer, ForeignKey('therapists.id'))
    therapists = relationship("Therapist", secondary=therapist_therapy_method, back_populates="therapy_methods")

class TherapyType(Base):
    """Data model for therapy types, calculated by Q&A flow."""
    __tablename__ = 'therapy_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False, unique=False)
    attributes = Column(String, nullable=True, unique=False)

# Database setup
DATABASE_URL = "sqlite:///./therapists.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)
