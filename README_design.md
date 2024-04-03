# Problem
API will be used to manage “projects”.

“Project” in our terminology is basically a plot of land, that we will be analyzing by utilizing the
satellite imagery captured in selected date range.

Supported operations:
- Create
- Read
- List
- Delete
- Update

Basic project attributes:
- name (required, character limit, up to 32 characters)
- description (optional)
- date range (required)
- area of interest (required, geojson file)

Technical requirements:
- FastAPI
- The projects have to be persisted
- [Optional] Test coverage
- [Optional] Provide dockerfile/docker-compose to run the application in a container

# Endpoints
**Base url:** `/api/v1`

## Create project
**Method:** `POST`

**URL:** `/projects`

**Request body:**
```json
{
  "name": "string",
  "description": "string",
  "date_range": ["string", "string"],
  "area_of_interest": {
     ...
  }
}
```

**Response:**
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "date_range": ["string", "string"],
  "area_of_interest": {
     ...
  }
}
```

## Read project
Since the API will finally require an authentication mechanism, the project will be read by its ID.
With no authentication, random hash should be used instead of the ID.

**Method:** `GET`

**URL:** `/projects/{project_id}`

**Response:**
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "date_range": ["string", "string"],
  "area_of_interest": {
     ...
  }
}
```

## List projects
**Method:** `GET`

**URL:** `/projects`

**Response:**

Storing the projects in the `"item"` field will allow for easy expansion of the response in the future (paging etc).
```json
"items": [
  {
    "id": "string",
    "name": "string",
    "description": "string",
    "date_range": ["string", "string"],
    "area_of_interest": {
       ...
    }
  }
]
```

## Update project
**Method:** `PUT`

**URL:** `/projects/{project_id}`

**Request body:**
```json
{
  "name": "string",
  "description": "string",
  "date_range": ["string", "string"],
  "area_of_interest": {
     ...
  }
}
```

**Response:**
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "date_range": ["string", "string"],
  "area_of_interest": {
     ...
  }
}
```

## Delete project
**Method:** `DELETE`

**URL:** `/projects/{project_id}`

**Response:**
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "date_range": ["string", "string"],
  "area_of_interest": {
     ...
  }
}
```

## Other considerations
- https://stackoverflow.com/questions/25970523/restful-what-should-a-delete-response-body-contain
- https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api

# Architecture

## Processing requests
- FastAPI will be used to handle the requests
- The application will use Uvicorn ASGI

## Data storage
- The projects will be stored in a PostgreSQL database
- The database will be accessed using the SQLAlchemy ORM

### Should the geojson file be stored in the database?
At this moment the exact requirements are not clear. It would mainly depend on the size of the files and frequency of access.

#### Storing in the database
**Pros:**
- Easier to manage and implement
- Transactions can be easily used to ensure consistency
- Stored as JSONB field (can even query the json)
- Fast
- Easy to backup

**Cons:**
- The database can become bloated and slow

#### Storing in the filesystem or an object storage like S3
**Pros:**
- Size of the geojson files will not affect the database and its performance
- Can store large files without any issues

**Cons:**
- Complex solution
- Can be more difficult to replicate to other regions of the world, depending on the implementation
- Significantly slower, might require API calls, especially when listing a lot of projects

### Conclusion
Following the rules of premature optimization/lean startup, the geojson files will be stored in the database. 
If the need arises, the implementation can be changed without too much trouble.

## Testing
Tests will be written using pytest and FastAPI's TestClient.

## Running and deploy
Dockerfile will be created to dockerize the application.

`docker-compose` will launch the application, postgres database and connect them using a network.

Bash script will be provided to easily build and run the application.

In the production enviroment, docker swarm or other orchestration tool will be used to deploy the application.