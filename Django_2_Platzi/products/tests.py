from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Products


class BaseAuthenticatedTestCase(TestCase):
    def create_and_login(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')


class ProductsTestCase(BaseAuthenticatedTestCase):
    def setUp(self):
        self.create_and_login()

        self.product = Products.objects.create(
            name="Martina",
            description="vieja amiga",
            category="mascota",
            price="200"
        )

    def test_products_have_name(self):
        martina = Products.objects.get(name="Martina")
        self.assertEqual(martina.description, self.product.description)


    def test_create_product(self):
        data = {
            'name': 'New Product',
            'description': 'This is a new product',
            'category': 'New Category',
            'price': 100
        }

        response = self.client.post('/product/new/', data)
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful form submission
        new_product = Products.objects.get(name='New Product')
        self.assertEqual(new_product.description, 'This is a new product')

    def test_create_product_logout(self):
        self.client.logout()
        data = {
            'name': 'New Product',
            'description': 'This is a new product',
            'category': 'New Category',
            'price': 100
        }

        url = '/product/new/'
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/login?next=/product/new/")

    def test_view_product_detail(self):
        url = f"/product/{self.product.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"luye me considera {self.product.description}", html=True)

    def test_view_product_detail_404(self):
        url = "/product/xxx/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_view_product_detail_without_login(self):
        self.client.logout()

        url = f"/product/{self.product.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            f"/login?next=/product/{self.product.id}/"
        )
