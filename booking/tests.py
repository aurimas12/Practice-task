from django.test import TestCase
from .models import (
    Booking,
    Bookable,
    BookableType,
    Team,
    Participation,
    Venue,
    Group,
    BookableTypeLimit,
)
from rest_framework import status
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


# class BookingViewSetTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username="admin", password="admin")
#         self.team = Team.objects.create(name="Black Team", url="black")
#         self.participation = Participation.objects.create(
#             role=1, team=self.team, account=self.user
#         )
#         self.bookabletype = BookableType.objects.create(bookable_type=1, name="strin2g")
#         self.bookable = Bookable.objects.create(
#             name="string", bookable_type_id=self.bookabletype, team_id=self.team
#         )
#         self.booking = Booking.objects.create(
#             date_from="2021-04-22T12:46:46.087Z",
#             date_to="2021-04-22T12:46:46.087Z",
#             bookable_id=self.bookable,
#             participant_id=self.participation,
#         )


#     def test_create_booking_then_overlapping_booking(self):
#         valid_data = {
#             "date_from": "2021-04-22T22:14:33.575Z",
#             "date_to": "2021-04-22T22:14:33.575Z",
#             "bookable_id": 1,
#             "participant_id": 1,
#         }
#         invalid_data = {
#             "date_from": "2021-04-22T12:46:46.087Z",
#             "date_to": "2021-04-22T22:14:33.575Z",
#             "bookable_id": 1,
#             "participant_id": 1,
#         }
#         client = Client()
#         response1 = client.post(
#             reverse("booking_create"),
#             data=valid_data,
#             content_type="application/json",
#         )
#         response2 = client.post(
#             reverse("booking_create"),
#             data=invalid_data,
#             content_type="application/json",
#         )

#         self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate


class BookingViewSetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="string", password="string")
        self.user.set_password("string")
        self.user.save()
        self.team = Team.objects.create(name="Black Team", url="black")
        self.venue1 = Venue.objects.create(
            name="test venue 1", parent_id=1, team_id=self.team
        )

        self.bookable_type = BookableType.objects.create(
            bookable_type=1, name="workspace"
        )
        self.group = Group.objects.create(name="group 1", issystem=True, isvisible=True)
        self.bookabletype = BookableType.objects.create(bookable_type=1, name="strin2g")
        self.bookable = Bookable.objects.create(
            name="string",
            bookable_type_id=self.bookabletype,
            team_id=self.team,
            venue_id=self.venue1,
        )
        self.bookable.group_id.add(self.group)
        self.bookable_type_limit = BookableTypeLimit.objects.create(
            workspace_limit=10, meeting_room_limit=10, parking_spot_limit=10
        )

    def test_bookable_create_endpoint(self):
        valid_data = {
            "name": "4",
            "bookable_type_id": self.bookabletype.id,
            "team_id": self.team.id,
            "venue_id": self.venue1.id,
            "group_id": [1],
        }
        client = APIClient()
        login = client.force_authenticate(self.user)

        response = client.post(
            reverse("bookable-create"),
            data=valid_data,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_team_all_endpoint(self):
        client = APIClient()
        login = client.force_authenticate(self.user)
        response = client.get(
            reverse("team-all"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)