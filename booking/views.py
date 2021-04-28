from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import BookableType, Bookable, Booking, BookableTypeLimit, Participation

from .serializers import (
    BookableTypeSerializer,
    BookableSerializer,
    BookingSerializer,
    BookableTypeLimitSerializer,
)

from src.services.BookingService import (
    check_date_from,
    user_role_limitations_for_created,
)
from src.services.BookableTypeLimitService import (
    get_workspace_count,
    get_meeting_room_count,
    get_parking_spot_count,
    check_request_bookable_type,
    get_bookable_types_limits,
    request_save_data,
    bookable_request_save_data,
)
from src.signals import create_post_signal
from src.services.ParticipantService import identity_roles, identity_account
from src.services.AuthenticationService import get_auth_user_name
from rest_framework import permissions


class BookableTypeLimitViewSet(viewsets.ModelViewSet):
    queryset = BookableTypeLimit.objects.all()
    serializer_class = BookableTypeLimitSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, **kwargs):
        queryset = BookableTypeLimit.objects.all()
        serializer = BookableTypeLimitSerializer(queryset, many=True)
        return Response(serializer.data)


class BookableTypeViewSet(viewsets.ModelViewSet):
    queryset = BookableType.objects.all()
    serializer_class = BookableTypeSerializer


class BookableViewSet(viewsets.ModelViewSet):
    queryset = Bookable.objects.all()
    serializer_class = BookableSerializer

    def create(self, request):
        serializer = BookableSerializer(data=request.data)
        request_bookable_type = check_request_bookable_type(request)
        workspace, meeting_room, car_spot = get_bookable_types_limits()

        if request_bookable_type == BookableType.TYPE_WORKSPACE:
            workspace_limit = get_workspace_count()
            if workspace < workspace_limit:
                return bookable_request_save_data(serializer, request)

        elif request_bookable_type == BookableType.TYPE_MEETING_ROOM:
            meeting_room_limit = get_meeting_room_count()
            if meeting_room < meeting_room_limit:
                return bookable_request_save_data(serializer, request)

        elif request_bookable_type == BookableType.TYPE_PARKING_SPOT:
            parking_spot_limit = get_parking_spot_count()
            if car_spot < parking_spot_limit:
                return bookable_request_save_data(serializer, request)

        return Response(create_post_signal())


from django.contrib.auth.models import User


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
            return request_save_data(serializer, request)

        elif Participation.ROLE_ASSISTANT == identity_account(user):

            if booking_type == BookableType.TYPE_WORKSPACE:

                if limits.workspace_limit > len(exist_booking):
                    return request_save_data(serializer, request)

            elif booking_type == BookableType.TYPE_MEETING_ROOM:

                if limits.meeting_room_limit > len(exist_booking):
                    return request_save_data(serializer, request)

            elif booking_type == BookableType.TYPE_PARKING_SPOT:

                if limits.parking_spot_limit > len(exist_booking):
                    return request_save_data(serializer, request)

        elif Participation.ROLE_USER == identity_account(user):
            if booking_type == BookableType.TYPE_WORKSPACE:
                if user_role_limitations_for_created(request) is True:

                    if limits.workspace_limit > len(exist_booking):
                        return request_save_data(serializer, request)

            elif booking_type == BookableType.TYPE_MEETING_ROOM:
                if user_role_limitations_for_created(request) is True:
                    if limits.meeting_room_limit > len(exist_booking):
                        return request_save_data(serializer, request)

            elif booking_type == BookableType.TYPE_PARKING_SPOT:
                if user_role_limitations_for_created(request) is True:
                    if limits.parking_spot_limit > len(exist_booking):
                        return request_save_data(serializer, request)

        return Response("No action!")
