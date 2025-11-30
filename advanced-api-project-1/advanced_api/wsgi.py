"""
WSGI config for advanced-api-project.

This module contains the WSGI application used by Django's development server and any WSGI-compatible web servers.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api.settings')

application = get_wsgi_application()
