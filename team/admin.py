from django.contrib import admin
from .models import Team, Participation, Venue

# Register your models here.
admin.site.register(Team)
admin.site.register(Participation)
admin.site.register(Venue)
