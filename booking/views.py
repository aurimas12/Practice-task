from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (
    BookableType,
    Bookable,
    Booking,
    BookableTypeLimit,
    Participation,
    Venue,
    TeamVenue,
)

from .serializers import (
    BookableTypeSerializer,
    BookableSerializer,
    BookingSerializer,
    BookableTypeLimitSerializer,
    TeamVenueSerializer,
)
from team.serializers import VenueSerializer
from src.services.BookingService import (
    check_date_from,
    user_role_limitations_for_created,
)

from src.services.BookableTypeLimitService import BookableTypeLimitService
from src.signals import create_post_signal
from src.services.ParticipantService import identity_roles, identity_account
from src.services.AuthenticationService import get_auth_user_name
from rest_framework import permissions
from django.contrib.auth.models import User


class BookableTypeLimitViewSet(viewsets.ModelViewSet):
    queryset = BookableTypeLimit.objects.all()
    serializer_class = BookableTypeLimitSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, **kwargs):
        queryset = BookableTypeLimit.objects.all()
        serializer = BookableTypeLimitSerializer(queryset, many=True)

        print("all users")
        print(User.objects.all()[0])
        return Response(serializer.data)


class BookableTypeViewSet(viewsets.ModelViewSet):
    queryset = BookableType.objects.all()
    serializer_class = BookableTypeSerializer


class BookableViewSet(viewsets.ModelViewSet):
    queryset = Bookable.objects.all()
    serializer_class = BookableSerializer

    def create(self, request):
        bookable_all = Bookable.objects.all()

        # venues = [i.venue_id.id for i in bookable_all]
        # status = request.data["venue_id"] in venues

        serializer = BookableSerializer(data=request.data)
        request_bookable_type = BookableTypeLimitService.check_request_bookable_type(
            request
        )
        (
            workspace,
            meeting_room,
            car_spot,
        ) = BookableTypeLimitService.get_bookable_types_limits()
        # if status == False:
        if request_bookable_type == BookableType.TYPE_WORKSPACE:
            workspace_limit = BookableTypeLimitService.get_workspace_count()
            if workspace < workspace_limit:
                return BookableTypeLimitService.bookable_request_save_data(
                    serializer, request
                )

        elif request_bookable_type == BookableType.TYPE_MEETING_ROOM:
            meeting_room_limit = BookableTypeLimitService.get_meeting_room_count()
            if meeting_room < meeting_room_limit:
                return BookableTypeLimitService.bookable_request_save_data(
                    serializer, request
                )

        elif request_bookable_type == BookableType.TYPE_PARKING_SPOT:
            parking_spot_limit = BookableTypeLimitService.get_parking_spot_count()
            if car_spot < parking_spot_limit:
                return BookableTypeLimitService.bookable_request_save_data(
                    serializer, request
                )

        return Response(create_post_signal())


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        permission_classes = (permissions.IsAuthenticated,)

        bookable_id = request.data["bookable_id"]
        user_id = request.data["participant_id"]

        bookable_obj = Bookable.objects.get(id=bookable_id)
        booking_type = bookable_obj.bookable_type_id.bookable_type

        role = identity_roles(Participation.objects.get(id=user_id))
        limits = BookableTypeLimit.objects.get(id=1)  # important
        exist_booking = Booking.objects.filter(bookable_id=bookable_id)  # important

        user = User.objects.get(id=request.user.id)

        if Participation.ROLE_ADMIN == identity_account(user):
            return BookableTypeLimitService.request_save_data(serializer, request)

        elif Participation.ROLE_ASSISTANT == identity_account(user):

            if booking_type == BookableType.TYPE_WORKSPACE:

                if limits.workspace_limit > len(exist_booking):
                    return BookableTypeLimitService.request_save_data(
                        serializer, request
                    )

            elif booking_type == BookableType.TYPE_MEETING_ROOM:

                if limits.meeting_room_limit > len(exist_booking):
                    return BookableTypeLimitService.request_save_data(
                        serializer, request
                    )

            elif booking_type == BookableType.TYPE_PARKING_SPOT:

                if limits.parking_spot_limit > len(exist_booking):
                    return BookableTypeLimitService.request_save_data(
                        serializer, request
                    )

        elif Participation.ROLE_USER == identity_account(user):
            if booking_type == BookableType.TYPE_WORKSPACE:
                if user_role_limitations_for_created(request) is True:

                    if limits.workspace_limit > len(exist_booking):
                        return BookableTypeLimitService.request_save_data(
                            serializer, request
                        )

            elif booking_type == BookableType.TYPE_MEETING_ROOM:
                if user_role_limitations_for_created(request) is True:
                    if limits.meeting_room_limit > len(exist_booking):
                        return BookableTypeLimitService.request_save_data(
                            serializer, request
                        )

            elif booking_type == BookableType.TYPE_PARKING_SPOT:
                if user_role_limitations_for_created(request) is True:
                    if limits.parking_spot_limit > len(exist_booking):
                        return BookableTypeLimitService.request_save_data(
                            serializer, request
                        )

        return Response("No action!")


class TeamVenueViewSet(viewsets.ModelViewSet):
    queryset = TeamVenue.objects.all()
    serializer_class = TeamVenueSerializer

    def list(self, request, **kwargs):

        items = Venue.objects.all()
        booking_obj = []
        list = []
        for item in items:
            venue_obj = Venue.objects.get(pk=item.id)
            bookable_obj = Bookable.objects.filter(venue_id=venue_obj.id)
            for i in bookable_obj:
                try:
                    booking_obj.append(Booking.objects.get(bookable_id=i.id))
                except:
                    break
            teamVenue = TeamVenue.objects.create(venue_id=venue_obj)
            teamVenue.bookable_id.set(bookable_obj)
            teamVenue.booking_id.set(booking_obj)
            booking_obj = []
        queryset = TeamVenue.objects.all()
        serializer = TeamVenueSerializer(queryset, many=True)
        return Response(serializer.data)
