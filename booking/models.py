from django.db import models
from team.models import Team,Participation
# Create your models here.
class BookableType(models.Model):
    TYPE_WORKSPACE = 1
    TYPE_MEETING_ROOM = 2
    TYPE_PARKING_SPOT = 3

    TYPE = (
        (TYPE_WORKSPACE, ('Workspace')),
        (TYPE_MEETING_ROOM, ('Meeting room')),
        (TYPE_PARKING_SPOT, ('Parking spot')),
    )

    bookable_type= models.PositiveSmallIntegerField(choices=TYPE)
    name=models.CharField(max_length=256)

class Bookable(models.Model):
    bookable_type_id=models.ForeignKey(BookableType, on_delete=models.CASCADE)
    name=models.CharField(max_length=256)
    team_id=models.ForeignKey(Team, on_delete=models.CASCADE)

class Booking(models.Model):
    bookable_id= models.ForeignKey(Bookable, on_delete=models.CASCADE)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    participant_id= models.ForeignKey(Participation, on_delete=models.CASCADE)