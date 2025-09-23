# Open ELIS v0.1 - API Documentation

## Introduction
Our goal is to lower the barrier to mental health access. 

This database provides you with information about therapists, their methods and locations. You are welcome to use the data in your own apps and non-commercial projects — like we did with creating this API.

This project is non-profit. 

## Endpoints
The API provides multiple endpoints. 

### GET /therapists

#### Purpose
Fetch a list of therapists, but limit the number of results to a maximum of 50 at a time.
Allow users to paginate through the data using limit and offset query parameters.

#### Query Parameters
- limit (int, optional): Specifies how many therapists to return. 
    - Default: 10
    - Maximum: 50
- offset (int, optional): Specifies how many records to skip (for pagination).
    - Default: 0
- district (str, optional): Filters the therapists by district.
- method (str, optional): Filters the therapists by therapy method.
- min_experience (int, optional): Filters the therapists by years of experience.

Each filter() call adds a condition to the SQL query.
These conditions are combined using AND logic in SQL.

For example, if the user provides district="District1", age_group="Adults", and method="Cognitive-Behavioral", the query will look like this:
```SQL
SELECT * FROM therapists
WHERE district = 'District1'
  AND age_group = 'Adults'
  AND method = 'Cognitive-Behavioral'
```


#### Validation Rules
- limit must be between 1 and 50.
- offset must be 0 or greater.

#### Response
A list of therapists (up to limit therapists).
Each therapist includes fields like id, first_name, last_name, email, etc.

#### Sample Request and Response
```Python
# Request
GET /therapists?limit=10&offset=20

# Response
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
