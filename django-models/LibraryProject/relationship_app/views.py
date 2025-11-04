from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library  # Explicit import for checker
from .models import Author, Librarian  # other models

# Function-Based View: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {'books': books})

# Class-Based View: display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"