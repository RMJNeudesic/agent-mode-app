# Simple REST API Documentation

This document describes the simple REST API endpoints that demonstrate basic REST API concepts.

## Overview

Two simple endpoints have been added to illustrate fundamental REST API principles:

1. **Health Check** - A simple GET endpoint that returns API status
2. **Echo** - A simple POST endpoint that echoes back the data sent

These endpoints are database-free and work without requiring MongoDB setup, making them ideal for demonstrating basic REST API concepts.

## Endpoints

### 1. Health Check Endpoint

**Purpose**: Returns the current status of the API. This is a common pattern used in production systems for health monitoring.

- **URL**: `/api/health/`
- **Method**: `GET`
- **Authentication**: Not required

**Example Request**:
```bash
curl http://localhost:8000/api/health/
```

**Example Response**:
```json
{
  "status": "healthy",
  "message": "OctoFit Tracker API is running",
  "version": "1.0.0"
}
```

**HTTP Status Code**: `200 OK`

**What it demonstrates**:
- Basic GET request handling
- JSON response formatting
- Simple status endpoint pattern

---

### 2. Echo Endpoint

**Purpose**: Returns the exact data sent in the request body. Useful for testing and demonstrating POST requests.

- **URL**: `/api/echo/`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Authentication**: Not required

**Example Request**:
```bash
curl -X POST http://localhost:8000/api/echo/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "message": "Hello, API!"}'
```

**Example Response**:
```json
{
  "received": {
    "name": "John Doe",
    "message": "Hello, API!"
  },
  "message": "Echo successful",
  "timestamp": "N/A"
}
```

**HTTP Status Code**: `200 OK`

**What it demonstrates**:
- POST request handling
- JSON request body parsing
- Request/response data flow
- Structured JSON responses

---

## Testing the Endpoints

### Using Python Test Client

A test script is provided in `/tmp/test_simple_api.py` that demonstrates how to test these endpoints:

```bash
cd octofit-tracker/backend
source venv/bin/activate
python /tmp/test_simple_api.py
```

### Using curl

After starting the Django development server:

```bash
cd octofit-tracker/backend
source venv/bin/activate
python manage.py runserver
```

Test the health check:
```bash
curl http://localhost:8000/api/health/
```

Test the echo endpoint:
```bash
curl -X POST http://localhost:8000/api/echo/ \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

### Using Django Test Framework

The endpoints have comprehensive unit tests in `octofit_tracker/tests.py`:

```python
class SimpleAPITest(APITestCase):
    def test_health_check_get(self):
        # Tests health check returns correct data
        
    def test_echo_post(self):
        # Tests echo returns posted data
        
    def test_echo_empty_post(self):
        # Tests echo handles empty data
        
    def test_health_check_wrong_method(self):
        # Tests method restriction on health check
        
    def test_echo_wrong_method(self):
        # Tests method restriction on echo
```

---

## HTTP Method Restrictions

Both endpoints enforce their allowed HTTP methods:

- **Health Check**: Only accepts `GET` requests
  - Other methods (POST, PUT, DELETE, etc.) return `405 Method Not Allowed`

- **Echo**: Only accepts `POST` requests
  - Other methods (GET, PUT, DELETE, etc.) return `405 Method Not Allowed`

This demonstrates proper REST API method handling and security.

---

## Error Handling

### Health Check Errors

- `405 Method Not Allowed`: If you try to use any method other than GET

### Echo Errors

- `405 Method Not Allowed`: If you try to use any method other than POST
- Invalid JSON will be handled by Django REST Framework and return appropriate error messages

---

## Integration with API Root

These endpoints are automatically listed in the API root endpoint at `/api/`:

```bash
curl http://localhost:8000/api/
```

Returns:
```json
{
  "users": "http://localhost:8000/api/users/",
  "teams": "http://localhost:8000/api/teams/",
  "activities": "http://localhost:8000/api/activities/",
  "leaderboard": "http://localhost:8000/api/leaderboard/",
  "workouts": "http://localhost:8000/api/workouts/",
  "health": "http://localhost:8000/api/health/",
  "echo": "http://localhost:8000/api/echo/"
}
```

---

## Key REST API Concepts Demonstrated

1. **HTTP Methods**: Proper use of GET and POST methods
2. **JSON Format**: Standard JSON request/response format
3. **Status Codes**: Appropriate HTTP status codes (200, 405)
4. **Endpoint Design**: Clear, meaningful endpoint URLs
5. **Method Restrictions**: Enforcing allowed methods per endpoint
6. **Stateless**: No session state required
7. **Self-documenting**: Responses include helpful messages

---

## Code Implementation

### View Functions (views.py)

```python
@api_view(['GET'])
def health_check(request):
    """Simple health check endpoint"""
    return Response({
        'status': 'healthy',
        'message': 'OctoFit Tracker API is running',
        'version': '1.0.0'
    })

@api_view(['POST'])
def echo(request):
    """Simple echo endpoint"""
    data = request.data
    return Response({
        'received': data,
        'message': 'Echo successful',
        'timestamp': request.META.get('HTTP_DATE', 'N/A')
    }, status=status.HTTP_200_OK)
```

### URL Configuration (urls.py)

```python
urlpatterns = [
    # ... other patterns ...
    path('api/health/', health_check, name='health-check'),
    path('api/echo/', echo, name='echo'),
]
```

---

## Benefits of These Simple Endpoints

1. **No Database Required**: Work without MongoDB setup
2. **Easy to Test**: Simple to verify with curl or any HTTP client
3. **Educational**: Clear demonstration of REST principles
4. **Production-Ready Pattern**: Health checks are used in real systems
5. **Fast Response**: No database queries means instant responses

---

## Next Steps

After understanding these simple endpoints, you can:

1. Explore the more complex endpoints (users, teams, activities, etc.)
2. Add authentication to these endpoints
3. Add request validation
4. Add rate limiting
5. Add response caching
6. Create more complex POST endpoints with data validation

---

## Troubleshooting

### Issue: 400 Bad Request

**Solution**: Make sure 'testserver' is in ALLOWED_HOSTS in settings.py

### Issue: 405 Method Not Allowed

**Solution**: Check you're using the correct HTTP method (GET for health, POST for echo)

### Issue: No response

**Solution**: Make sure the Django development server is running on port 8000

---

For more information, see the Django REST Framework documentation: https://www.django-rest-framework.org/
