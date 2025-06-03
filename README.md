# M-ko Event Management API Documentation

## Overview

The M-ko Event Management API is a FastAPI-based REST API for managing events. It provides endpoints for creating, reading, updating, and deleting events, as well as adding reviews to events.

**Base URL**: https://mko-backend.onrender.com
**Version**: 1.0.0
**Database**: SQLite with SQLAlchemy ORM

## Authentication

Currently, this API does not require authentication. All endpoints are publicly accessible.

## CORS

The API is configured to accept requests from any origin with CORS enabled for all methods and headers.

---

## Endpoints

### Health Check

#### GET `/`
Returns basic API information.

**Response:**
```json
{
  "message": "Event Management API",
  "version": "1.0.0"
}
```

#### GET `/health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy"
}
```

---

### Events

#### GET `/events/`
Retrieve all events.

**Query Parameters:**
- `skip` (int, optional): Number of records to skip (default: 0, min: 0)
- `limit` (int, optional): Number of records to return (default: 100, min: 1, max: 1000)

**Response:** Array of Event objects

**Example Request:**
```bash
GET /events/?skip=0&limit=10
```

**Example Response:**
```json
[
  {
    "id": 1,
    "image": "https://admin.ticketmojo.co.ke//storage/events/main_photo_1746873032.jpg",
    "name": "Project X!",
    "genre": "Music",
    "date": "2025-06-27",
    "location": "TBA",
    "organizer": "House of Music Entertainment",
    "rating": 5.0,
    "reviews": [],
    "description": null,
    "ticket": "https://ticketmojo.co.ke/event/project-x!#buy-ticket"
  }
]
```

#### POST `/events/`
Create a new event.

**Request Body:** Event creation object

**Response:** Created Event object (HTTP 201)

**Example Request:**
```json
{
  "name": "Summer Music Festival",
  "genre": "Music",
  "date": "2025-07-15",
  "location": "Central Park",
  "organizer": "Music Events Co",
  "rating": 4.5,
  "description": "A fantastic summer music festival",
  "ticket": "https://example.com/tickets"
}
```

#### GET `/events/{event_id}`
Retrieve a specific event by its ID.

**Path Parameters:**
- `event_id` (int): The unique identifier of the event

**Response:** Event object

**Example Request:**
```bash
GET /events/1
```

**Error Responses:**
- `404`: Event not found

#### PUT `/events/{event_id}`
Update an existing event.

**Path Parameters:**
- `event_id` (int): The unique identifier of the event

**Request Body:** Event update object (partial updates supported)

**Response:** Updated Event object

**Example Request:**
```json
{
  "name": "Updated Event Name",
  "location": "New Venue"
}
```

**Error Responses:**
- `404`: Event not found
- `400`: Invalid data provided

#### DELETE `/events/{event_id}`
Delete an event.

**Path Parameters:**
- `event_id` (int): The unique identifier of the event

**Response:**
```json
{
  "message": "Event deleted",
  "id": 1
}
```

**Error Responses:**
- `404`: Event not found
- `400`: Unable to delete event

---

### Reviews

#### POST `/events/{event_id}/review`
Add a review to a specific event.

**Path Parameters:**
- `event_id` (int): The unique identifier of the event

**Request Body:** Review object (flexible structure)

**Example Request:**
```json
{
  "rating": 4,
  "comment": "Great event, really enjoyed it!",
  "reviewer": "John Doe"
}
```

**Response:**
```json
{
  "message": "Review added",
  "reviews": [
    {
      "rating": 4,
      "comment": "Great event, really enjoyed it!",
      "reviewer": "John Doe",
      "timestamp": "2025-06-03T10:30:00.123456"
    }
  ]
}
```

**Error Responses:**
- `404`: Event not found
- `400`: Invalid review data

---

## Data Models

### Event Schema

#### EventCreate (Request)
```json
{
  "image": "string (max 1000 chars, optional)",
  "name": "string (required, 1-255 chars)",
  "genre": "string (max 100 chars, optional)", 
  "date": "string (required, YYYY-MM-DD format)",
  "location": "string (max 500 chars, optional)",
  "organizer": "string (max 255 chars, optional)",
  "rating": "float (0-5, default: 5.0, optional)",
  "reviews": "array (default: [], optional)",
  "description": "string (optional)",
  "ticket": "string (max 1000 chars, optional)"
}
```

#### EventUpdate (Request)
All fields are optional for partial updates:
```json
{
  "image": "string (max 1000 chars, optional)",
  "name": "string (1-255 chars, optional)",
  "genre": "string (max 100 chars, optional)",
  "date": "string (YYYY-MM-DD format, optional)",
  "location": "string (max 500 chars, optional)",
  "organizer": "string (max 255 chars, optional)",
  "rating": "float (0-5, optional)",
  "reviews": "array (optional)",
  "description": "string (optional)",
  "ticket": "string (max 1000 chars, optional)"
}
```

#### EventResponse (Response)
```json
{
  "id": "integer (auto-generated)",
  "image": "string or null",
  "name": "string",
  "genre": "string or null",
  "date": "string (YYYY-MM-DD)",
  "location": "string or null",
  "organizer": "string or null", 
  "rating": "float",
  "reviews": "array",
  "description": "string or null",
  "ticket": "string or null"
}
```

---

## Sample Data

The API comes pre-loaded with sample events including:
- Music events (Project X!, Soul-Tie, RNB Soul Out)
- Food events (Motherland Brunch)
- Traditional events (Mambo Jangor)
- Technology events (Landing Pages Workshop)
- Sports events (Chibweza Cup)
- Party events (Launch Party, Drinks on Deck)
- Film events (Anime Watch Party)

---

## Error Handling

The API returns appropriate HTTP status codes:

- `200`: Success
- `201`: Created successfully
- `400`: Bad request (validation errors, malformed data)
- `404`: Resource not found
- `422`: Validation error (Pydantic validation failed)
- `500`: Internal server error

Error responses follow this format:
```json
{
  "detail": "Error description"
}
```

---

## Validation Rules

### Date Format
- Must be in `YYYY-MM-DD` format
- Example: `"2025-06-27"`

### Rating
- Must be between 0 and 5 (inclusive)
- Supports decimal values (e.g., 4.5)

### String Length Limits
- Event name: 1-255 characters (required)
- Genre: max 100 characters
- Location: max 500 characters
- Organizer: max 255 characters
- Image URL: max 1000 characters
- Ticket URL: max 1000 characters

---

## Usage Examples

### Create an Event
```bash
curl -X POST "your-api-url/events/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Tech Conference 2025",
    "genre": "Technology", 
    "date": "2025-09-15",
    "location": "Convention Center",
    "organizer": "TechCorp",
    "description": "Annual technology conference"
  }'
```

### Get Events with Pagination
```bash
curl "your-api-url/events/?skip=10&limit=5"
```

### Update an Event
```bash
curl -X PUT "your-api-url/events/1" \
  -H "Content-Type: application/json" \
  -d '{
    "location": "Updated Venue Name"
  }'
```

### Add a Review
```bash
curl -X POST "your-api-url/events/1/review" \
  -H "Content-Type: application/json" \
  -d '{
    "rating": 5,
    "comment": "Amazing event!",
    "reviewer": "Jane Smith"
  }'
```

---

## Deployment

This API is designed to be deployed on Render with the following configuration:
- Runtime: Python
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

The database (SQLite) is automatically created and initialized with sample data on startup.
