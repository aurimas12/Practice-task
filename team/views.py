from .models import Team, Participation, Venue
from booking.models import Bookable, Booking
from .serializers import (
    TeamSerializer,
    ParticipantSerializer,
    VenueSerializer,
)
from rest_framework.response import Response
from rest_framework import viewsets


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipantSerializer


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
