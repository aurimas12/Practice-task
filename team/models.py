from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Team(models.Model):
    members = models.ManyToManyField(User, through="Participation")
    name = models.CharField(max_length=255, validators=[])
    url = models.SlugField(max_length=64, validators=[])
    logo = models.ImageField(upload_to="", blank=True, null=True)

    def __str__(self):
        return self.name


class Participation(models.Model):
    """
    Participation intermediary model.
    Connects Team with Account as many to many.
    """

    ROLE_ADMIN = 1
    ROLE_ASSISTANT = 2
    ROLE_USER = 3

    ROLE = (
        (ROLE_ADMIN, ("Admin")),
        (ROLE_ASSISTANT, ("Assistant")),
        (ROLE_USER, ("User")),
    )

    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="participations"
    )
    account = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="participations"
    )
    role = models.PositiveSmallIntegerField(choices=ROLE)


class Venue(models.Model):
    name = models.CharField(max_length=125)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="venue")
    parent_id = models.PositiveSmallIntegerField(blank=True)
