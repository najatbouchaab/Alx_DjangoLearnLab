from rest_framework import serializers
from api.models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

# Test cases for the serializers
from rest_framework.exceptions import ValidationError
from django.test import TestCase

class AuthorSerializerTest(TestCase):
    def test_author_serializer_with_books(self):
        author = Author.objects.create(name="Author Name")
        Book.objects.create(title="Book Title", publication_year=2021, author=author)
        
        serializer = AuthorSerializer(author)
        self.assertEqual(serializer.data, {
            'id': author.id,
            'name': author.name,
            'books': [{'id': 1, 'title': 'Book Title', 'publication_year': 2021, 'author': author.id}]
        })

class BookSerializerTest(TestCase):
    def test_book_serializer(self):
        author = Author.objects.create(name="Author Name")
        book = Book.objects.create(title="Book Title", publication_year=2021, author=author)
        
        serializer = BookSerializer(book)
        self.assertEqual(serializer.data, {
            'id': book.id,
            'title': book.title,
            'publication_year': book.publication_year,
            'author': author.id
        })

    def test_invalid_book_serializer(self):
        serializer = BookSerializer(data={'title': '', 'publication_year': 2021})
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)