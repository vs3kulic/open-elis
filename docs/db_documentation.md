# Database Documentation

## Overview
The database design follows established practices for relational modeling and is implemented using SQLAlchemy. It is normalized to Third Normal Form (3NF), ensuring scalability, data integrity, and efficient querying.

---

## Key Features

### **Normalization**
- The database is normalized to 3NF:
  - Each table has a clear primary key.
  - Relationships between entities are properly normalized into separate tables (e.g., `TherapistContact`, `TherapistAddress`, `therapist_therapy_method`).
  - No redundant or transitive dependencies.

### **Relationships**
- **One-to-One Relationships**:
  - `TherapistContact` and `TherapistAddress` are linked to `Therapist` using `uselist=False`.
  - `TherapyType` and `TherapyMethodCluster` are linked with a one-to-one relationship.
- **One-to-Many Relationships**:
  - `Therapist` ↔ `TherapistAddress` allows therapists to have multiple addresses.
- **Many-to-Many Relationships**:
  - `Therapist` ↔ `TherapyMethod` is handled via the `therapist_therapy_method` association table.

### **Scalability**
- The design is scalable:
  - Adding new therapy methods, clusters, or types is straightforward.
  - Relationships are flexible and can accommodate future changes (e.g., additional contact methods or therapy types).

### **SQLAlchemy Best Practices**
- **Declarative Base**:
  - Models are defined declaratively using the `Base` class.
- **Relationships**:
  - `back_populates` ensures bidirectional navigation between related models.
- **Foreign Keys**:
  - Foreign keys enforce referential integrity between tables.
- **Association Table**:
  - The `therapist_therapy_method` table manages many-to-many relationships.

### **Database Setup**
- **Engine and Session Management**:
  - The `SessionLocal` factory is set up for managing database sessions.
- **Table Creation**:
  - `Base.metadata.create_all(bind=engine)` ensures tables are created automatically.
