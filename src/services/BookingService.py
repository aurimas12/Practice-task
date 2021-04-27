from src.exceptions.bookingException import BadRequestException
from booking.models import Booking, Participation


def check_date_from(request):
    data = Booking.objects.filter(date_from=request.data["date_from"])
    if data.exists():
        raise BadRequestException("'Booking date from exist,choice another date")


def user_role_limitations_for_created(request):
    role = Participation.ROLE_USER
    data = request.data["participant_id"]
    participant = Participation.objects.get(id=data)
    participant_role = participant.role

    if role == participant_role:
        return True
