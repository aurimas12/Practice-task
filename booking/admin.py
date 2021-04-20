from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BookableType)
admin.site.register(Bookable)
admin.site.register(Booking)
