from rest_framework import serializers
from .models import BookableType, Bookable, Booking, BookableTypeLimit, TeamVenue
from django.contrib.auth.models import User
from team.models import Team, Participation


class BookableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookableType
        fields = ["id", "bookable_type", "name"]


class BookableTypeLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookableTypeLimit
        fields = "__all__"


class BookableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookable
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class TeamVenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamVenue
        fields = "__all__"
