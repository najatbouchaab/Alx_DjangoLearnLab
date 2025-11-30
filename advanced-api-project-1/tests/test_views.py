from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Author, Book

class BookViewSetTests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(title="Book 1", publication_year=2021, author=self.author)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'Book 2',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'Book 2')

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {
            'title': 'Updated Book 1',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book 1')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)