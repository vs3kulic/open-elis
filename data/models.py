from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

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
    __tablename__ = "therapists"

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    title = Column(String, nullable=True)
    registration_date = Column(Date, nullable=False)
    registration_number = Column(Integer, nullable=False, unique=True)
    therapy_methods = relationship("TherapyMethod", secondary=therapist_therapy_method, back_populates="therapist")
    contacts = relationship("TherapistContact", back_populates="therapist", uselist=False)
    addresses = relationship("TherapistAddress", back_populates="therapist", uselist=False)

class TherapistContact(Base):
    """Data model for therapist contact methods."""
    __tablename__ = "therapist_contacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    website = Column(String, nullable=True) # until we have more data
    therapist_id = Column(Integer, ForeignKey("therapists.id"), nullable=False)
    therapist = relationship("Therapist", back_populates="contacts")

class TherapistAddress(Base):
    """Data model for therapist addresses."""
    __tablename__ = "therapist_addresses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    state = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    therapist_id = Column(Integer, ForeignKey("therapists.id"), nullable=False)
    therapist = relationship("Therapist", back_populates="addresses") # one-to-many

class TherapyMethod(Base):
    """Data model for therapy methods, as indicated by source data."""
    __tablename__ = "therapy_methods"

    id = Column(Integer, primary_key=True, autoincrement=True)
    method_name = Column(String, nullable=False, unique=False)
    cluster_id = Column(Integer, ForeignKey("therapy_method_clusters.id"), nullable=False)
    therapy_cluster = relationship("TherapyMethodCluster", back_populates="methods", uselist=False)
    therapist = relationship("Therapist", secondary=therapist_therapy_method, back_populates="therapy_methods")

class TherapyMethodCluster(Base):
    """Data model for therapy clusters, as per official documentation."""
    __tablename__ = "therapy_method_clusters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cluster_short = Column(String, nullable=False, unique=True)
    cluster_name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True, unique=False)
    methods = relationship("TherapyMethod", back_populates="therapy_cluster")

class TherapyType(Base):
    """Data model for therapy types, calculated by Q&A flow."""
    __tablename__ = "therapy_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_short = Column(String, nullable=False, unique=True)
    type_name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False, unique=False)
    cluster_id = Column(Integer, ForeignKey("therapy_method_clusters.id"), nullable=False)
    therapy_cluster = relationship("TherapyMethodCluster", back_populates="therapy_type", uselist=False)


# Database setup
DATABASE_URL = "sqlite:///./therapists.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)
print("Database tables created successfully.")
