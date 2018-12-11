from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(1, len(b.posts))
        self.assertEqual('Test Post', b.posts[0].title)
        self.assertEqual('Test Content', b.posts[0].content)