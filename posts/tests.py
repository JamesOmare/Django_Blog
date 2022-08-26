from django.test import TestCase
from .models import Post
# Create your tests here.

class PostTestCase(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title = 'test title',
            author = 'test author',
            content = 'test content'
        )

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Test template
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'List of posts')


    def test_create_post(self):
        post_to_test = Post.objects.get(id=1)
        post_title = f'{post_to_test.title}'

        self.assertEqual(self.post.title, post_title)
        self.assertEqual(self.post.title, 'test title')
        self.assertEqual(self.post.author, 'test author')