from django.test import TestCase
from rest_framework import status
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSetTestCase(TestCase):
    def setUp(self):
        pass

    def test_request_authentication(self):
        client = Client()
        response = client.get(reverse("test_user"), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
