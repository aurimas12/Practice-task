from rest_framework import serializers
from .models import BookableType,Bookable, Booking


class BookableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookableType
        fields = '__all__'

class BookableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookable
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'