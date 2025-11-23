# API Documentation

## Overview
This document provides an overview of the API endpoints available in the `api_project`. The API is built using Django REST Framework and supports CRUD operations for managing resources.

## Base URL
The base URL for the API is:
```
http://localhost:8000/api/
```

## Endpoints

### 1. List Books
- **URL:** `/books/`
- **Method:** `GET`
- **Description:** Retrieve a list of all books.
- **Response:**
  - **200 OK**
  - Content: A JSON array of book objects.

### 2. Create a Book
- **URL:** `/books/`
- **Method:** `POST`
- **Description:** Create a new book.
- **Request Body:**
  - Content-Type: `application/json`
  - Example:
    ```json
    {
      "title": "Book Title",
      "author": "Author Name"
    }
    ```
- **Response:**
  - **201 Created**
  - Content: The created book object.

### 3. Retrieve a Book
- **URL:** `/books/{id}/`
- **Method:** `GET`
- **Description:** Retrieve a specific book by ID.
- **Response:**
  - **200 OK**
  - Content: The book object.

### 4. Update a Book
- **URL:** `/books/{id}/`
- **Method:** `PUT`
- **Description:** Update a specific book by ID.
- **Request Body:**
  - Content-Type: `application/json`
  - Example:
    ```json
    {
      "title": "Updated Book Title",
      "author": "Updated Author Name"
    }
    ```
- **Response:**
  - **200 OK**
  - Content: The updated book object.

### 5. Delete a Book
- **URL:** `/books/{id}/`
- **Method:** `DELETE`
- **Description:** Delete a specific book by ID.
- **Response:**
  - **204 No Content**

## Authentication
The API supports token-based authentication. Users must obtain a token by logging in and include it in the `Authorization` header for protected endpoints.

## Permissions
Access to certain endpoints may be restricted based on user permissions. Ensure that the appropriate permissions are set for each view.

## Error Handling
The API returns standard HTTP status codes for errors:
- **400 Bad Request:** Invalid input.
- **404 Not Found:** Resource not found.
- **403 Forbidden:** Access denied.

## Conclusion
This API provides a simple interface for managing books. For further details on usage, refer to the codebase or the Django REST Framework documentation.