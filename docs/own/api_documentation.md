# Open ELIS v0.1 - API Documentation

## Introduction
Open ELIS is a non-profit project aimed at lowering the barriers to mental health access. This API provides information about therapists, their methods, and locations. It is designed for use in apps and non-commercial projects.

## Endpoints

### GET /therapists

#### Purpose
Retrieve a list of therapists with optional filtering and pagination.

#### HTTP Method
GET

#### URL
`/therapists`

#### Query Parameters
- `limit` (int, optional): Number of therapists to return per request.
  - Default: 10
- `offset` (int, optional): Number of records to skip for pagination.
  - Minimum: 0
  - Default: 0
- `postal_code` (str, optional): Filter therapists by postal code.
- `therapy_method` (str, optional): Filter therapists by therapy method name.
- `min_experience` (int, optional): Filter therapists by minimum years of experience.

#### Validation Rules
- `limit` must be a positive integer.
- `offset` must be 0 or greater.
- `min_experience` filters therapists registered at least N years ago.
- `therapy_method` must match exact therapy method names in the database.
- `postal_code` must match Austrian postal code format.

#### Response
A JSON array of therapists, each containing the following fields:
- `id` (int): Unique identifier.
- `first_name` (str): Therapist's first name.
- `last_name` (str): Therapist's last name.
- `email` (str): Therapist's email address.
- `state` (str): State where the therapist is located.
- `postal_code` (str): Postal code of the therapist's location.
- `therapy_methods` (str): Therapy methods offered by the therapist.

#### Sample Requests
```http
# Basic pagination
GET /therapists?limit=10&offset=20

# Filter by postal code and therapy method
GET /therapists?postal_code=1010&therapy_method=Verhaltenstherapie

# Filter by minimum experience (therapists registered 5+ years ago)
GET /therapists?min_experience=5
```

#### Sample Response
```json
[
    {
        "id": 21,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "state": "W",
        "postal_code": "1010",
        "therapy_methods": "Existenzanalyse"
    },
    {
        "id": 22,
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com",
        "state": "N",
        "postal_code": "4020",
        "therapy_methods": "Verhaltenstherapie"
    }
]
```

---

### GET /therapy_methods

#### Purpose
Retrieve a list of therapy methods with optional filtering and pagination.

#### HTTP Method
GET

#### URL
`/therapy_methods`

#### Query Parameters
- `limit` (int, optional): Number of therapy methods to return per request.
  - Default: 25
- `offset` (int, optional): Number of records to skip for pagination.
  - Minimum: 0
  - Default: 0
- `method_name` (str, optional): Filter by exact therapy method name.
- `therapy_cluster` (str, optional): Filter by therapy cluster short code (PA, HT, ST, VT).

#### Response
A JSON array of therapy methods, each containing:
- `id` (int): Unique identifier.
- `method_name` (str): Name of the therapy method.
- `cluster_id` (int): ID of the associated therapy cluster.
- `therapy_cluster` (object): Related cluster information.

#### Sample Requests
```http
# Get all therapy methods
GET /therapy_methods

# Filter by cluster (Verhaltenstherapeutisch)
GET /therapy_methods?therapy_cluster=PA

# Search for specific method
GET /therapy_methods?method_name=Daseinsanalyse
```

#### Sample Response
```json
[
    {
        "id": 1,
        "method_name": "Verhaltenstherapie",
        "cluster_id": 4
    },
    {
        "id": 2,
        "method_name": "Existenzanalyse",
        "cluster_id": 2,
    }
]
```

---

### GET /therapy_clusters

#### Purpose
Retrieve a list of therapy clusters with optional filtering and pagination.

#### HTTP Method
GET

#### URL
`/therapy_clusters`

#### Query Parameters
- `limit` (int, optional): Number of therapy clusters to return per request.
  - Default: 10
- `offset` (int, optional): Number of records to skip for pagination.
  - Minimum: 0
  - Default: 0
- `cluster_short` (str, optional): Filter by exact therapy cluster short code (e.g., PA, HT, ST, VT).

#### Response
A JSON array of therapy clusters, each containing:
- `id` (int): Unique identifier.
- `cluster_name` (str): Full name of the therapy cluster.
- `cluster_short` (str): Short code for the therapy cluster.

#### Sample Requests
```http
# Get all therapy clusters
GET /therapy_clusters

# Filter by cluster short code
GET /therapy_clusters?cluster_short=PA
```

#### Sample Response
```json
[
    {
        "id": 1,
        "cluster_name": "Psychoanalytisch",
        "cluster_short": "PA"
    },
    {
        "id": 2,
        "cluster_name": "Humanistisch",
        "cluster_short": "HT"
    }
]
```

---

### GET /therapy_types

#### Purpose
Retrieve a list of therapy types with optional filtering and pagination.

#### HTTP Method
GET

#### URL
`/therapy_types`

#### Query Parameters
- `limit` (int, optional): Number of therapy types to return per request.
  - Default: 10
- `offset` (int, optional): Number of records to skip for pagination.
  - Minimum: 0
  - Default: 0
- `cluster_short` (str, optional): Filter by therapy cluster short code (PA, HT, ST, VT).

#### Response
A JSON array of therapy types, each containing:
- `id` (int): Unique identifier.
- `type_name` (str): Full name of the therapy type.
- `type_short` (str): Short code for the therapy type.
- `description` (str): Description of the therapy type.
- `cluster_id` (int): ID of the associated therapy cluster.

#### Sample Requests
```http
# Get all therapy types
GET /therapy_types

# Filter by cluster short code
GET /therapy_types?cluster_short=VT
```

#### Sample Response
```json
[
    {
        "id": 1,
        "type_name": "Cognitive Behavioral Therapy",
        "type_short": "CBT",
        "description": "A form of psychological treatment that focuses on changing negative thought patterns",
        "cluster_id": 4
    },
    {
        "id": 2,
        "type_name": "Psychodynamic Therapy",
        "type_short": "PDT",
        "description": "A therapeutic approach based on psychoanalytic principles",
        "cluster_id": 1
    }
]
```

---

## Therapy Clusters Reference

| Short Code | Full Name | Description |
|------------|-----------|-------------|
| PA | Psychoanalytisch | Psychoanalytic approaches |
| HT | Humanistisch | Humanistic approaches |
| ST | Systemisch | Systemic approaches |
| VT | Verhaltenstherapeutisch | Behavioral approaches |

## Error Handling
- **400 Bad Request**: Invalid query parameters.
- **404 Not Found**: No results found matching the criteria.
- **500 Internal Server Error**: Unexpected server error.

## Rate Limiting
Currently no rate limiting is implemented. Please use responsibly.

## Changelog
- **v0.1**: Initial release with `/therapists`, `/therapy_methods`, `/therapy_clusters`, and `/therapy_types` endpoints.
