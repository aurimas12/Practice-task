from rest_framework import viewsets, status
from .models import BookableType, Bookable, Booking, BookableTypeLimit
from .serializers import (
    BookableTypeSerializer,
    BookableSerializer,
    BookingSerializer,
    BookableTypeLimitSerializer,
)
from rest_framework.response import Response
from src.services.BookingService import check_date_from
from rest_framework.decorators import action

from rest_framework.decorators import api_view
from rest_framework.views import APIView


class BookableTypeLimitViewSet(viewsets.ModelViewSet):
    queryset = BookableTypeLimit.objects.all()
    serializer_class = BookableTypeLimitSerializer


class BookableTypeViewSet(viewsets.ModelViewSet):
    queryset = BookableType.objects.all()
    serializer_class = BookableTypeSerializer


class BookableViewSet(viewsets.ModelViewSet):
    queryset = Bookable.objects.all()
    serializer_class = BookableSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            check_date_from(request)
            serializer.save()
            return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
