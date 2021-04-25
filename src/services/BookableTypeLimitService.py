from src.exceptions.bookingException import BadRequestException
from booking.models import BookableType


def get_meeting_room_count(bookable_type_id):
    return len(BookableType.objects.filter(bookable_type=bookable_type_id))
