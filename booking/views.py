from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import BookableType, Bookable, Booking, BookableTypeLimit, Participation

from .serializers import (
    BookableTypeSerializer,
    BookableSerializer,
    BookingSerializer,
    BookableTypeLimitSerializer,
)

from src.services.BookingService import check_date_from
from src.services.BookableTypeLimitService import (
    get_workspace_count,
    get_meeting_room_count,
    get_parking_spot_count,
    check_request_bookable_type,
    get_bookable_types_limits,
    request_save_data,
)
from src.signals import create_post_signal
from src.services.ParticipantService import identity_roles


class BookableTypeLimitViewSet(viewsets.ModelViewSet):
    queryset = BookableTypeLimit.objects.all()
    serializer_class = BookableTypeLimitSerializer

    def list(self, request):
        queryset = BookableTypeLimit.objects.all()
        serializer = BookableTypeLimitSerializer(queryset, many=True)
        participation = Participation.objects.get(id=1)
        print(identity_roles(participation))
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
                request_save_data(serializer)

        elif request_bookable_type == BookableType.TYPE_MEETING_ROOM:
            meeting_room_limit = get_meeting_room_count()
            if meeting_room < meeting_room_limit:
                request_save_data(serializer)

        elif request_bookable_type == BookableType.TYPE_PARKING_SPOT:
            parking_spot_limit = get_parking_spot_count()
            if car_spot < parking_spot_limit:
                request_save_data(serializer)

        return Response(create_post_signal())


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        bookable_id = request.data["bookable_id"]
        user_id = request.data["participant_id"]
        role = identity_roles(Participation.objects.get(id=user_id))
        bookable_obj = Bookable.objects.get(id=bookable_id)
        booking_type = bookable_obj.bookable_type_id.bookable_type

        limits = BookableTypeLimit.objects.get(id=1)  # important
        exist_booking = Booking.objects.filter(bookable_id=bookable_id)  # important
        if Participation.ROLE_ADMIN == role[0]:
            if serializer.is_valid():
                check_date_from(request)
                serializer.save()
                return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
        elif Participation.ROLE_ASSISTANT == role[0]:
            if booking_type == 1:
                if limits.workspace_limit > len(exist_booking):
                    if serializer.is_valid():
                        check_date_from(request)
                        serializer.save()
                        return Response(
                            {"msg": "Data Created"}, status=status.HTTP_201_CREATED
                        )
                return Response("Bad request data")
            elif booking_type == 2:
                if limits.meeting_room_limit > len(exist_booking):
                    if serializer.is_valid():
                        check_date_from(request)
                        serializer.save()
                        return Response(
                            {"msg": "Data Created"}, status=status.HTTP_201_CREATED
                        )
                    return Response("Bad request data")
            elif booking_type == 3:
                if limits.parking_spot_limit > len(exist_booking):
                    if serializer.is_valid():
                        check_date_from(request)
                        serializer.save()
                        return Response(
                            {"msg": "Data Created"}, status=status.HTTP_201_CREATED
                        )
                    return Response("Bad request data")
        elif Participation.ROLE_USER == role[0]:
            if booking_type == 1:
                if limits.workspace_limit > len(exist_booking):
                    if serializer.is_valid():
                        check_date_from(request)
                        serializer.save()
                        return Response(
                            {"msg": "Data Created"}, status=status.HTTP_201_CREATED
                        )
                return Response("Bad request data")
            elif booking_type == 2:
                if limits.meeting_room_limit > len(exist_booking):
                    if serializer.is_valid():
                        check_date_from(request)
                        serializer.save()
                        return Response(
                            {"msg": "Data Created"}, status=status.HTTP_201_CREATED
                        )
                    return Response("Bad request data")
            elif booking_type == 3:
                if limits.parking_spot_limit > len(exist_booking):
                    if serializer.is_valid():
                        check_date_from(request)
                        serializer.save()
                        return Response(
                            {"msg": "Data Created"}, status=status.HTTP_201_CREATED
                        )
                    return Response("Bad request data")

        return Response("nieko nevyksta")
