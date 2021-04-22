from django.test import TestCase
from .models import Booking, Bookable, BookableType, Team, Participation
from rest_framework import status
from django.test.client import Client
from django.urls import reverse
from booking.serializers import BookableTypeSerializer
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
        self.data = Booking.objects.create(
            date_from="2021-04-22T12:46:46.087Z",
            date_to="2021-04-22T12:46:46.087Z",
            bookable_id=self.bookable,
            participant_id=self.participation,
        )

    def test_data(self):
        self.assertEqual(2, 2)
