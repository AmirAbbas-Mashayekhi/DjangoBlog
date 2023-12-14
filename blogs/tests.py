from django.test import TestCase
from django.shortcuts import reverse
from .models import Blog, Author


class UrlTest(TestCase):

    def url_testing_template(self, url_or_name: str, use_name=False):
        if not use_name:
            response = self.client.get(url_or_name)
        else:
            response = self.client.get(reverse(url_or_name))
        self.assertEquals(response.status_code, 200)

    def test_home_page(self):
        self.url_testing_template('')

    def test_blogs_page(self):
        self.url_testing_template('blog_index', use_name=True)


class DatabaseTest(TestCase):
    def setUp(self):
        Author.objects.create(
            user_name='test',
            first_name='test Author',
            last_name='test Author',
            email='test@gmail.com',
            password='1234'
        )
        self.blog = Blog.objects.create(
            title='Test Blog',
            text='lorem ipsum dolor sit amet.',
            author=Author.objects.get(user_name='test'),
            status=Blog.STATUS_POSTED
        )

    def test_blog_details_page(self):
        response = self.client.get(reverse('blog_info', args=[self.blog.id]))
        self.assertEquals(response.status_code, 200)
