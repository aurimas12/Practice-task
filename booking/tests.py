from django.test import TestCase
from .models import BookableType
from rest_framework import status


class ShopTestCase(TestCase):
    def setUp(self):
        pass

    def test_add_to_cart(self):
        self.assertEqual(1, 1)
