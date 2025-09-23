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
- **limit** (int, optional): Number of therapists to return per request.
  - Default: 10
  - Maximum: 50
- **offset** (int, optional): Number of records to skip for pagination.
  - Default: 0
  - Minimum: 0
- **district** (str, optional): Filter therapists by district.
- **method** (str, optional): Filter therapists by therapy method.
- **min_experience** (int, optional): Filter therapists by minimum years of experience.

#### Validation Rules
- `limit` must be between 1 and 50.
- `offset` must be 0 or greater.

#### Response
A JSON array of therapists, each containing the following fields:
- `id` (int): Unique identifier.
- `first_name` (str): Therapist's first name.
- `last_name` (str): Therapist's last name.
- `email` (str): Therapist's email address.
- `state` (str): State where the therapist is located.
- `postal_code` (str): Postal code of the therapist's location.
- `therapy_methods` (str): Therapy methods offered by the therapist.

#### Sample Request
```http
GET /therapists?limit=10&offset=20
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

## Error Handling
- **400 Bad Request**: Invalid query parameters.
- **404 Not Found**: No therapists found matching the criteria.
- **500 Internal Server Error**: Unexpected server error.

## Changelog
- **v0.1**: Initial release with `/therapists` endpoint.
