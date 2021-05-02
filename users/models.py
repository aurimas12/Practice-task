from django.db import models
from group.models import Group
from django.contrib.auth.models import User

# Create your models here.
class UserGroup(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ManyToManyField(Group, blank=True)
