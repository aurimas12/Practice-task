from django.test import TestCase
from .models import Booking, Bookable, BookableType, Team, Participation
from rest_framework import status
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class ShopTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="admin", password="admin")
        self.team = Team.objects.create(name="Black Team", url="black")
        self.participation = Participation.objects.create(
            role=1, team=self.team, account=self.user
        )
        self.bookabletype = BookableType.objects.create(bookable_type=1, name="strin2g")
        self.bookable = Bookable.objects.create(
            name="string", bookable_type_id=self.bookabletype, team_id=self.team
        )
        self.booking = Booking.objects.create(
            date_from="2021-04-22T12:46:46.087Z",
            date_to="2021-04-22T12:46:46.087Z",
            bookable_id=self.bookable,
            participant_id=self.participation,
        )

    def test_data(self):
        valid_data = {
            "date_from": "2021-04-22T22:14:33.575Z",
            "date_to": "2021-04-22T22:14:33.575Z",
            "bookable_id": 1,
            "participant_id": 1,
        }
        invalid_data = {
            "date_from": "2021-04-22T12:46:46.087Z",
            "date_to": "2021-04-22T22:14:33.575Z",
            "bookable_id": 1,
            "participant_id": 1,
        }
        client = Client()
        response1 = client.post(
            reverse("booking_create"),
            data=valid_data,
            content_type="application/json",
        )
        response2 = client.post(
            reverse("booking_create"),
            data=invalid_data,
            content_type="application/json",
        )
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)