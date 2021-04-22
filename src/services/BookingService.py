from src.exceptions.bookingException import BadRequestException
from booking.models import Booking


def check_date_from(request):
    data = Booking.objects.filter(date_from=request.data["date_from"])
    if data.exists():
        raise BadRequestException("'Booking date from exist,choice another date")
