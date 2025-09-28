# ELIS Database Documentation

## Overview
A normalized SQLAlchemy-based database for managing Austrian therapists and their therapy methods. Designed for the ELIS therapy matching platform.

## Schema Design

### Core Entities
- **Therapists**: Licensed therapy practitioners in Austria
- **Therapy Methods**: Specific therapeutic techniques/approaches
- **Therapy Method Clusters**: Grouped therapy methods (e.g., Verhaltenstherapie)  
- **Therapy Types**: High-level categories derived from Q&A matching

### Design Principles
- **3NF Normalized**: No redundant data, proper entity separation
- **Referential Integrity**: All relationships enforced via foreign keys
- **Unidirectional Relationships**: Where business logic dictates (TherapyType → TherapyMethodCluster)

## Entity Relationships

### Mandatory Relationships (nullable=False)
| From | To | Type | Description |
|------|----|----- |-------------|
| TherapistContact | Therapist | 1:1 | Every contact belongs to one therapist |
| TherapistAddress | Therapist | 1:1 | Every address belongs to one therapist |
| TherapyMethod | TherapyMethodCluster | N:1 | Every method belongs to one cluster |
| TherapyType | TherapyMethodCluster | N:1 | Every type references one cluster |

### Optional Relationships
| From | To | Type | Description |
|------|----|----- |-------------|
| Therapist | TherapyMethod | N:N | Therapists can practice multiple methods (via junction table) |

## Data Model

```sql
-- Core therapist information
therapists (
    id INTEGER PRIMARY KEY,
    last_name STRING NOT NULL,
    first_name STRING NOT NULL, 
    title STRING,
    registration_date DATE NOT NULL,
    registration_number INTEGER UNIQUE NOT NULL
)

-- One contact record per therapist
therapist_contacts (
    id INTEGER PRIMARY KEY,
    email STRING NOT NULL,
    website STRING,
    therapist_id INTEGER NOT NULL → therapists.id
)

-- One address record per therapist  
therapist_addresses (
    id INTEGER PRIMARY KEY,
    state STRING NOT NULL,
    postal_code STRING NOT NULL,
    therapist_id INTEGER NOT NULL → therapists.id
)

-- Therapy method clusters (official categories)
therapy_method_clusters (
    id INTEGER PRIMARY KEY,
    cluster_short STRING UNIQUE NOT NULL,
    cluster_name STRING UNIQUE NOT NULL,
    description STRING
)

-- Individual therapy methods
therapy_methods (
    id INTEGER PRIMARY KEY,
    method_name STRING NOT NULL,
    cluster_id INTEGER NOT NULL → therapy_method_clusters.id
)

-- High-level therapy types (from matching algorithm)
therapy_types (
    id INTEGER PRIMARY KEY,
    type_short STRING UNIQUE NOT NULL,
    type_name STRING UNIQUE NOT NULL,
    description STRING NOT NULL,
    cluster_id INTEGER NOT NULL → therapy_method_clusters.id
)

-- Junction table for therapist-method relationships
therapist_therapy_method (
    therapist_id INTEGER → therapists.id,
    therapy_method_id INTEGER → therapy_methods.id,
    PRIMARY KEY (therapist_id, therapy_method_id)
)
```

### Key Design Decisions

1. **Unidirectional TherapyType → TherapyMethodCluster**
   - Every therapy type must belong to a cluster
   - Clusters can exist without assigned therapy types
   - Prevents circular dependencies in the matching algorithm

2. **Mandatory Contact/Address per Therapist**
   - Ensures data completeness for user-facing features
   - Simplifies frontend logic (no null checks needed)

3. **Many-to-Many Therapist ↔ TherapyMethod**
   - Reflects real-world practice where therapists use multiple approaches
   - Enables flexible filtering and matching

## Technical Notes

- **Database**: SQLite for development, easily portable to PostgreSQL
- **ORM**: SQLAlchemy with declarative base
- **Migrations**: Manual schema updates via `Base.metadata.create_all()`
- **Session Management**: Factory pattern with `SessionLocal`

---

*Last updated: September 2025*

