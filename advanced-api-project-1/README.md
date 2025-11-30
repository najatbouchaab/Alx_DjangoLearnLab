# Advanced API Project

This project is a Django application that utilizes Django REST Framework to create a robust API for managing books and authors. It demonstrates advanced API development techniques, including custom serializers and complex data handling.

## Project Structure

```
advanced-api-project/
├── manage.py                # Command-line utility for interacting with the Django project
├── requirements.txt         # Project dependencies
├── advanced_api/            # Main Django application
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI entry point
├── api/                     # API application
│   ├── models.py            # Data models for the application
│   ├── serializers.py       # Custom serializers for models
│   ├── views.py             # API views for CRUD operations
│   ├── urls.py              # API endpoint routing
│   ├── filters.py           # Filtering capabilities for the API
│   └── migrations/          # Database migrations
│       └── __init__.py
├── tests/                   # Test suite for the application
│   ├── __init__.py
│   ├── test_models.py       # Unit tests for models
│   ├── test_serializers.py   # Unit tests for serializers
│   └── test_views.py        # Unit tests for views
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd advanced-api-project
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Start the development server:**
   ```
   python manage.py runserver
   ```

## API Functionality

The API provides endpoints for managing books and authors, including:

- **Books:**
  - List all books
  - Create a new book
  - Retrieve a specific book
  - Update a book
  - Delete a book

- **Authors:**
  - List all authors
  - Create a new author
  - Retrieve a specific author
  - Update an author
  - Delete an author

## Testing

To run the test suite, use the following command:

```
python manage.py test
```

This will execute all unit tests defined in the `tests` directory, ensuring the integrity and functionality of the application.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.