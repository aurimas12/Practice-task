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
    test,
)


class BookableTypeLimitViewSet(viewsets.ModelViewSet):
    queryset = BookableTypeLimit.objects.all()
    serializer_class = BookableTypeLimitSerializer

    def list(self, request):
        queryset = BookableTypeLimit.objects.all()
        serializer = BookableTypeLimitSerializer(queryset, many=True)
        # business logic for create booking - if reach max limit cant booking
        # check or can booking
        # parking_spot_limits = get_meeting_room_count(3)
        # limit = BookableTypeLimit.objects.all()
        # # seria = BookableTypeLimitSerializer(limit, many=False)
        # # limit = seria.data
        # limit = limit[0].parking_spot_limit

        # limits parking spots
        parking_spot_limit = get_parking_spot_count()

        # get all bookables
        # x = Bookable.objects.all()
        # # get bookable type id
        # ids = []

        # for i in x:
        #     # print(i, i.id, i.bookable_type_id)
        #     ids.append((i.bookable_type_id))
        # # same bookable type calc count
        # workspace = 0
        # meeting_room = 0
        # car_spot = 0
        # for i in ids:
        #     if i.bookable_type == BookableType.TYPE_WORKSPACE:
        #         workspace += 1
        #     elif i.bookable_type == BookableType.TYPE_MEETING_ROOM:
        #         meeting_room += 1
        #     elif i.bookable_type == BookableType.TYPE_PARKING_SPOT:
        #         car_spot += 1
        #     print(i.bookable_type)
        workspace, meeting_room, car_spot = test()
        # print(x)
        # print(ids[0].bookable_type)
        print("--------------")
        print("workspace", workspace)
        print("meeting room", meeting_room)
        print("car spot", car_spot)

        # check or can create new bookable

        # # get all Bookables
        # # x = Bookable.objects.all()
        # # seria = BookableSerializer(x, many=True)
        # # for i in seria.data:
        # #     print(i)
        # # print("******")
        # # show every type how much reserv
        # # cars_spot= Bookable.objects.filter(bookable_type_id=3)
        # # meeting_room= Bookable.objects.filter(bookable_type_id=2)
        # # workspace= Bookable.objects.filter(bookable_type_id=1)
        # bookables_count = get_bookable_type_count(3)
        # print(limit, bookables_count)
        # cars_spot = Bookable.objects.all()

        # for i in cars_spot:
        #     # print("bookable id:", i.id)
        #     print(1)
        #     value = BookableType.objects.get(id=i.id)
        #     print("bookable type", value.bookable_type)
        #     print("****")
        # cars_spot_count = Bookable.objects.filter(bookable_type_id=3)
        # meeting_room_count = Bookable.objects.filter(bookable_type_id=2)
        # workspace_count = Bookable.objects.filter(bookable_type_id=1)
        # print("car spot:", cars_spot_count)
        # print("meeting room:", meeting_room_count)
        # print("workspace:", workspace_count)
        # booking_count = Booking.objects.filter()
        # print(parking_spot_limits)
        return Response(serializer.data)


class BookableTypeViewSet(viewsets.ModelViewSet):
    queryset = BookableType.objects.all()
    serializer_class = BookableTypeSerializer


class BookableViewSet(viewsets.ModelViewSet):
    queryset = Bookable.objects.all()
    serializer_class = BookableSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            check_date_from(request)
            serializer.save()
            return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
