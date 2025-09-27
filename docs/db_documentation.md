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
  - `TherapyType` and `TherapyMethodCluster` are linked with a unidirectional relationship.
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
  - `back_populates` ensures bidirectional navigation between related models where necessary.
- **Foreign Keys**:
  - Foreign keys enforce referential integrity between tables.
- **Association Table**:
  - The `therapist_therapy_method` table manages many-to-many relationships.

### **Database Setup**
- **Engine and Session Management**:
  - The `SessionLocal` factory is set up for managing database sessions.
- **Table Creation**:
  - `Base.metadata.create_all(bind=engine)` ensures tables are created automatically.

---

## Analysis of Optional Relationships

### **Criteria for Optional Relationships**
A relationship is considered optional if:
1. The foreign key column allows `NULL` values (default behavior unless explicitly set to `nullable=False`).
2. The parent model does not enforce the existence of the related child model.

### **Optional Relationships in the Current Schema**

1. **Therapist ↔ TherapistContact**
   - **Status**: Mandatory
   - **Reason**: The `therapist_id` column in `TherapistContact` is explicitly set to `nullable=False`, ensuring that every `TherapistContact` must be linked to a `Therapist`.

2. **Therapist ↔ TherapistAddress**
   - **Status**: Mandatory
   - **Reason**: The `therapist_id` column in `TherapistAddress` is explicitly set to `nullable=False`, ensuring that every `TherapistAddress` must be linked to a `Therapist`.

3. **Therapist ↔ TherapyMethod**
   - **Status**: Optional
   - **Reason**: This is a many-to-many relationship managed via the `therapist_therapy_method` association table. Many-to-many relationships are inherently optional.

4. **TherapyMethod ↔ TherapyMethodCluster**
   - **Status**: Mandatory
   - **Reason**: The `cluster_id` column in `TherapyMethod` is explicitly set to `nullable=False`, ensuring that every `TherapyMethod` must be linked to a `TherapyMethodCluster`.

5. **TherapyMethodCluster ↔ TherapyType**
   - **Status**: Optional
   - **Reason**: A `TherapyMethodCluster` does not need to have an associated `TherapyType`.

6. **TherapyType ↔ TherapyMethodCluster**
   - **Status**: Mandatory
   - **Reason**: The `cluster_id` column in `TherapyType` is explicitly set to `nullable=False`, ensuring that every `TherapyType` must be linked to a `TherapyMethodCluster`.

### **Summary Table**

| **Relationship**                          | **Optional?** | **Reason**                                                                 |
|-------------------------------------------|---------------|-----------------------------------------------------------------------------|
| **Therapist ↔ TherapistContact**          | No            | `therapist_id` is `nullable=False`, enforcing the relationship.             |
| **Therapist ↔ TherapistAddress**          | No            | `therapist_id` is `nullable=False`, enforcing the relationship.             |
| **Therapist ↔ TherapyMethod**             | Yes           | Many-to-many relationships are inherently optional.                        |
| **TherapyMethod ↔ TherapyMethodCluster**  | No            | `cluster_id` is `nullable=False`, enforcing the relationship.               |
| **TherapyType ↔ TherapyMethodCluster**    | No            | `cluster_id` is `nullable=False`, enforcing the relationship.               |

---

## TherapyMethodCluster ↔ TherapyType Relationship

The relationship between `TherapyMethodCluster` and `TherapyType` has been simplified to be unidirectional. This means:

- **Mandatory Relationship**: Every `TherapyType` must reference a `TherapyMethodCluster` via the `cluster_id` foreign key. This is enforced by setting `nullable=False` on the `cluster_id` column in the `TherapyType` model.
- **Optional Relationship**: A `TherapyMethodCluster` does not need to have an associated `TherapyType`. This reflects the real-world scenario where not all therapy clusters are assigned a specific therapy type.

#### **Rationale for Simplification**
1. **Avoid Unnecessary Complexity**: The bidirectional relationship was not required for the application's use case.
2. **Align with Business Logic**: The design ensures that every therapy type is part of a cluster, but clusters can exist independently of therapy types.
3. **Improved Maintainability**: Simplifying the relationship reduces the potential for errors and makes the schema easier to understand and maintain.

#### **Updated Schema**
- The `TherapyMethodCluster` model no longer includes the `therapy_type` relationship.
- The `TherapyType` model retains the `cluster_id` foreign key and the `therapy_cluster` relationship for navigation.

