from django.test import TestCase
from .models import Author, Message

# Create your tests here.
class AuthorModelTest(TestCase):
    def test_author_creation(self):
        Author.objects.create(name='test', password='test')
        self.assertEqual(Author.objects.count(), 1)

class MessageModelTest(TestCase):
    def test_message_creation(self):
        author = Author.objects.create(name='test', password='test')
        Message.objects.create(author=author, content='test')
        self.assertEqual(Message.objects.count(), 1)