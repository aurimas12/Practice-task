from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import BookableType, Bookable, Booking, BookableTypeLimit

from .serializers import (
    BookableTypeSerializer,
    BookableSerializer,
    BookingSerializer,
    BookableTypeLimitSerializer,
)
from src.services.BookingService import check_date_from
from src.services.BookableTypeLimitService import (
    # get_meeting_room_count,
    get_bookable_type_count,
    get_parking_spot_count,
    check_request_bookable_type,
    get_bookable_types_limits,
)


class BookableTypeLimitViewSet(viewsets.ModelViewSet):
    queryset = BookableTypeLimit.objects.all()
    serializer_class = BookableTypeLimitSerializer

    def list(self, request):
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
        print(request_bookable_type)

        parking_spot_limit = get_parking_spot_count()
        workspace, meeting_room, car_spot = get_bookable_types_limits()

        if (
            request_bookable_type == BookableType.TYPE_WORKSPACE
        ):  # create workspace request data save
            pass
        elif (
            request_bookable_type == BookableType.TYPE_MEETING_ROOM
        ):  # create workspace request data save
            pass
        elif request_bookable_type == BookableType.TYPE_PARKING_SPOT:
            if car_spot < parking_spot_limit:
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {"msg": "Data Created"}, status=status.HTTP_201_CREATED
                    )
            else:
                print("no free place")  # create response msg
        else:
            print("Can't booking car place! All cars spot used")  # create response msg

        return Response("nieko nevyksta")


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            check_date_from(request)
            serializer.save()
            return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
