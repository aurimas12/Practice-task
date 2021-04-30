from rest_framework import serializers
from .models import (
    BookableType,
    Bookable,
    Booking,
    BookableTypeLimit,
    Group,
)
from group.serializers import GroupSerializer
from django.contrib.auth.models import User


from django.db import models
from team.models import Team, Participation
from group.models import Group


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


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
        # fields = ("bookable_type_id", "name", "team_id", "group")


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    # validators
    # def validate_date_from(self, value):
    #     date_from = Booking.objects.filter(date_from=value)
    #     if date_from.exists():
    #         raise serializers.ValidationError("This date from is exist")
    #     return value
