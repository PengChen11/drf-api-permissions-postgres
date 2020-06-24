from django.test import TestCase
from django.contrib.auth.models import User

from .models import News


class NewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        # Create a news post
        test_post = News.objects.create(
            user=testuser1,
            title='test news title',
            source='test.com',
            date='2020-06-22',
            url='apple.com',
            body='Body content...')
        test_post.save()

    def test_blog_content(self):
        post = News.objects.get(id=1)
        expected_user = f'{post.user}'
        expected_source = f'{post.source}'
        expected_date = f'{post.date}'
        expected_url = f'{post.url}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_user, 'testuser1')
        self.assertEqual(expected_source, 'test.com')
        self.assertEqual(expected_date, '2020-06-22')
        self.assertEqual(expected_url, 'apple.com')
        self.assertEqual(expected_title, 'test news title')
        self.assertEqual(expected_body, 'Body content...')
