from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products


@skip("demostrating skipping")
class TestSkip(TestCase):
    def test_skip_sample(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name="django", slug="django")
        User.objects.create_user(username="paul")
        Product.objects.create(
            category_id=1,
            title="django beginners",
            created_by_id=1,
            image="django",
            slug="django-beginners",
            price="20.2",
        )

    # def test_url_allowed_hosts(self):
    #     """
    #     Test homepage response status
    #     """
    #     response = self.c.get("/")
    #     self.assertEqual(response.status_code, 200)

    # @skip("demostrating skipping")
    def test_product_detail_url(self):
        """
        Test product detail response status
        """
        response = self.c.get(
            reverse("store:product_detail", args=["django-beginners"])
        )
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test category detail response status
        """
        response = self.c.get(reverse("store:category_list", args=["django"]))
        self.assertEqual(response.status_code, 200)

    # this is a test for the views using the HttpRequest object to send requests to the views
    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode("utf8")
        print(html)
        self.assertIn("<title>BookStore</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get("/django-beginners")
        response = all_products(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>BookStore</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_url_allowed_hosts(self):
        """
        Test Allowed hosts
        """
        response = self.c.get("/", HTTP_HOST="noaddress.com")
        self.assertEqual(response.status_code, 400)
        response = self.c.get("/", HTTP_HOST="yourdomain.com")
        self.assertEqual(response.status_code, 200)
