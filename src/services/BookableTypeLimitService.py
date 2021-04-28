from src.exceptions.bookingException import BadRequestException
from booking.models import BookableType, Bookable, BookableTypeLimit
from rest_framework.response import Response
from rest_framework import viewsets, status
from src.services.AuthenticationService import get_auth_user_name
from src.services.BookingService import check_date_from


def get_workspace_count():
    value = BookableTypeLimit.objects.all()
    return value[0].parking_spot_limit


def get_meeting_room_count():
    value = BookableTypeLimit.objects.all()
    return value[0].parking_spot_limit


def get_parking_spot_count():
    value = BookableTypeLimit.objects.all()
    return value[0].parking_spot_limit


def get_bookable_types_limits():
    workspace = 0
    meeting_room = 0
    car_spot = 0
    ids = []
    bookables = Bookable.objects.all()

    for i in bookables:
        ids.append(i.bookable_type_id)

    for i in ids:
        if i.bookable_type == BookableType.TYPE_WORKSPACE:
            workspace += 1
        elif i.bookable_type == BookableType.TYPE_MEETING_ROOM:
            meeting_room += 1
        elif i.bookable_type == BookableType.TYPE_PARKING_SPOT:
            car_spot += 1
    return workspace, meeting_room, car_spot


def check_request_bookable_type(request):
    request_bookable_type_id = request.data["bookable_type_id"]
    bookable = BookableType.objects.get(id=request_bookable_type_id)
    return bookable.bookable_type


def request_save_data(serializer, request):
    if serializer.is_valid():
        check_date_from(request)
        serializer.save()
        username = get_auth_user_name(request)
        return Response(
            {"msg": str(username) + " created data"},
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response("No action!")
