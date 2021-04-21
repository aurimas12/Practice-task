from rest_framework import serializers
from .models import BookableType,Bookable,Booking


class BookableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookableType
        fields = '__all__'