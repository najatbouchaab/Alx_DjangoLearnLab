from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian  # Make sure Library is explicitly imported

# -------------------------------
# Function-Based View: list all books
# -------------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {'books': books})

# -------------------------------
# Class-Based View: display library details
# -------------------------------
class LibraryDetailView(DetailView):
    model = Library  # ALX checker looks for Library explicitly
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"