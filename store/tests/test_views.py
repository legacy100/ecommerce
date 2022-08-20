from unittest import skip

from django.test import TestCase, Client

from django.contrib.auth.models import User
from django.http import HttpRequest
from store.models import Product, Category

from django.urls import reverse

# @skip("demostrating skipping")
# class TestSkip(TestCase):
#     def test_skip_sample(self):
#         pass

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name="django", slug="django")
        User.objects.create_user(username="paul")
        Product.objects.create(category_id=1, title="django beginners", created_by_id=1, image="django", slug="django-beginners", price="20.2")

    def test_url_allowed_hosts(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    # @skip("demostrating skipping")
    def test_product_detail_url(self):
        """
        Test product detail response status
        """
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)


    def test_category_detail_url(self):
        """
        Test category detail response status
        """
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    
    def test_homepage_html(self):
        request = HttpRequest()