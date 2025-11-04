
from django.urls import path
from .views import list_books  # Function-based view
from .views import LibraryDetailView  # Class-based view

from .views import register_view, login_view, logout_view  # Authentication views
from .views import admin_view, librarian_view, member_view  # Role-based views

urlpatterns = [
    # Function-based and Class-based views for books and libraries
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # User Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Role-Based Access Control URLs
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]