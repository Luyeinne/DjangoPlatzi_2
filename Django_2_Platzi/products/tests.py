from django.test import TestCase
from .models import Products

class ProductsTestCase(TestCase):
    def setUp(self):
        Products.objects.create(
            name= "Martina",
            description = "vieja amiga",
            category = "mascota",
            price = "200"
        )

    def test_products_have_name(self):
        martina = Products.objects.get(name="Martina")

        self.assertEqual(martina.description, "vieja amiga")

