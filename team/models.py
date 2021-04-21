from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):
    members = models.ManyToManyField(User, through='Participation')
    name = models.CharField(max_length=255, validators=[])
    url = models.SlugField(max_length=64, validators=[])  # Should be Unique? Of course
    logo = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.name
        
class Participation(models.Model):
    """
    Participation intermediary model.
    Connects Team with Account as many to many.
    """
    ROLE_PARTICIPANT = 1
    ROLE_ADMINISTRATOR = 2
    ROLE_OWNER = 3

    # private field
    ROLE = (
        (ROLE_PARTICIPANT, ('Participant')),
        (ROLE_ADMINISTRATOR, ('Administrator')),
        (ROLE_OWNER, ('Owner')),
    )

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='participations')
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    role = models.PositiveSmallIntegerField(choices=ROLE)

    def __str__(self):
        return self.account.username

