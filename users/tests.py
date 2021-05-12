from django.test import TestCase
from rest_framework import status
import requests


# class KongAuthorizationTestCase(TestCase):
# def test_get_access_token(self):
#     payload = {
#         "client_id": "456",
#         "client_secret": "789",
#         "grant_type": "client_credentials",
#     }
#     result = requests.post(
#         "https://kong:8443/mockbin/oauth2/token?key=123",
#         data=payload,
#         verify=False,
#     )
#     self.assertEqual(result.status_code, status.HTTP_200_OK)

# def test_endpoint_with_access_token(self):
#     payload = {
#         "client_id": "456",
#         "client_secret": "789",
#         "grant_type": "client_credentials",
#     }
#     result = requests.post(
#         "https://kong:8443/mockbin/oauth2/token?key=123",
#         data=payload,
#         verify=False,
#     )
#     access_token = result.json()["access_token"]
#     headers = {
#         "content-type": "application/json",
#         "authorization": "Bearer " + access_token,
#     }
#     result1 = requests.post("http://kong:8000/mockbin?key=123", headers=headers)
#     self.assertEqual(result1.status_code, status.HTTP_200_OK)

# def test_unauthorized(self):
#     result = requests.get("http://kong:8000/api/team")
#     self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)
