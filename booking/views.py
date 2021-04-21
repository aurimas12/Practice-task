from rest_framework import viewsets
from .models import *
from .serializers import *

class BookableTypeViewSet(viewsets.ModelViewSet):
    queryset=BookableType.objects.all()
    serializer_class= BookableTypeSerializer

class BookableViewSet(viewsets.ModelViewSet):
    queryset=Bookable.objects.all()
    serializer_class= BookableSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class= BookingSerializer    