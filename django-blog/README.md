# Django Blog Project

This is a simple blog application built with Django. It allows users to create, read, update, and delete blog posts. The project includes a basic setup with models, views, templates, and static files.

## Features

- List of blog posts
- Detailed view of each blog post
- Basic styling with CSS
- Admin interface for managing posts

## Project Structure

```
django-blog/
├── blog/                  # Blog application
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── static/            # Static files (CSS, JS)
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # Application configuration
│   ├── models.py          # Data models
│   ├── tests.py           # Tests for the application
│   ├── urls.py            # URL routing for the blog app
│   └── views.py           # View functions
├── config/                # Project configuration
│   ├── __init__.py        # Package marker
│   ├── asgi.py            # ASGI configuration
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL routing for the project
│   └── wsgi.py            # WSGI configuration
├── manage.py              # Command-line utility for managing the project
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-blog
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Usage

- Use the Django admin interface to create and manage blog posts.
- Visit the homepage to see the list of recent posts.
- Click on a post title to view its details.

## License

This project is licensed under the MIT License.