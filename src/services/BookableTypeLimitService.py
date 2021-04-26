from src.exceptions.bookingException import BadRequestException
from booking.models import BookableType, Bookable, BookableTypeLimit


def get_parking_spot_count():
    value = BookableTypeLimit.objects.all()

    return value[0].parking_spot_limit


def get_bookable_type_count(bookable_type_id):
    bookables = Bookable.objects.all()
    count = 0
    for i in bookables:
        # print("bookable id:", i.id)
        print(1)
        value = BookableType.objects.get(id=i.id)
        print(value)
        # print("bookable type", value.bookable_type, "-", bookable_type_id)
        print("****")
        if value.bookable_type == bookable_type_id:
            print(value)

    print(len(bookables))
    return count


def get_bookable_types_limits():
    workspace = 0
    meeting_room = 0
    car_spot = 0
    # get all bookables
    x = Bookable.objects.all()
    ids = []

    for i in x:
        # print(i, i.id, i.bookable_type_id)
        ids.append((i.bookable_type_id))
    for i in ids:
        if i.bookable_type == BookableType.TYPE_WORKSPACE:
            workspace += 1
        elif i.bookable_type == BookableType.TYPE_MEETING_ROOM:
            meeting_room += 1
        elif i.bookable_type == BookableType.TYPE_PARKING_SPOT:
            car_spot += 1
        print(i.bookable_type)
    return workspace, meeting_room, car_spot


def check_request_bookable_type(request):
    request_bookable_type_id = request.data["bookable_type_id"]
    print("*****")

    print(request_bookable_type_id)
    a = BookableType.objects.get(id=request_bookable_type_id)
    print(a.bookable_type)
    return a.bookable_type