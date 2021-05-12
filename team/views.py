from .models import Team, Participation, Venue
from booking.models import Bookable, Booking
from .serializers import TeamSerializer, ParticipantSerializer, VenueSerializer
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

    # def list_venues_paths(self, request, **kwargs):
    #     serializer_class = TeamSerializer
    #     items = Venue.objects.all()
    #     booking_obj = []
    #     list = []
    #     for item in items:
    #         venue_obj = Venue.objects.get(pk=item.id)
    #         bookable_obj = Bookable.objects.filter(venue_id=venue_obj.id)
    #         for i in bookable_obj:
    #             try:
    #                 booking_obj.append(Booking.objects.get(bookable_id=i.id))
    #             except:
    #                 break
    #         list.append([(venue_obj), (bookable_obj), (booking_obj)])
    #         booking_obj = []

    #     return Response(str(list))
