from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Test Post', content='This is a test post.', author='Author Name')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'Test Post')

    def test_content(self):
        post = Post.objects.get(id=1)
        expected_object_content = f'{post.content}'
        self.assertEqual(expected_object_content, 'This is a test post.')

    def test_author(self):
        post = Post.objects.get(id=1)
        expected_object_author = f'{post.author}'
        self.assertEqual(expected_object_author, 'Author Name')