from unittest import TestCase
from blog import Blog
from post import Post

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Blog', 'Kinhos')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Blog by Kinhos (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Blog', 'Kinhos')
        b.posts = ['Post fake']
        b2.posts = ['Post fake', 'Post de mentira']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Blog by Kinhos (2 posts)')


    def test_create_post(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual([Post('Test Post', 'Test Content')], b.posts)

    def test_json(self):
        b = Blog('Test', 'Test Author')

        expected_dict = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [],
        }

        self.assertDictEqual(expected_dict, b.json())