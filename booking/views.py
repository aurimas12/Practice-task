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
        data = request.data

        # participation info
        result = identity_roles(Participation.objects.get(id=data["participant_id"]))

        # booking info

        bookable = Bookable.objects.get(id=data["bookable_id"])

        bookable_type_number = bookable.bookable_type_id.bookable_type

        limit = BookableTypeLimit.objects.get(id=1)

        print("***")
        workspace, meeting_room, car_spot = get_bookable_types_limits()

        """start logic"""
        # 1.Get Status
        result = identity_roles(Participation.objects.get(id=data["participant_id"]))
        # request_bookable_type = check_request_bookable_type(request)
        # workspace, meeting_room, car_spot = get_bookable_types_limits()

        if result == Participation.ROLE_ADMIN:
            print("admin")
            if serializer.is_valid():
                check_date_from(request)
                serializer.save()
                return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
        elif result == Participation.ROLE_ASSISTANT:
            print(limit.parking_spot_limit)

            count_bookables = len(
                Bookable.objects.filter(bookable_type_id=BookableType.TYPE_PARKING_SPOT)
            )
            print(car_spot)
            print(count_bookables)
            if limit.parking_spot_limit > count_bookables:
                if serializer.is_valid():
                    check_date_from(request)
                    serializer.save()
                    return Response(
                        {"msg": "Data Created"}, status=status.HTTP_201_CREATED
                    )
            else:
                return Response("No empty places!")
            # if count_bookables<
            return Response("Assistant business logic")
        elif result == Participation.ROLE_USER:
            # only parking
            print("user")

        return Response("nieko nevyksta")
