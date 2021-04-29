from django.db import models

# Create your models here.
class Group(models.Model):
    # id
    name = models.CharField(max_length=128)
    issystem = models.BooleanField(default=False)
    isvisible = models.BooleanField(default=False)
