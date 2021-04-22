from rest_framework import viewsets, status
from .models import BookableType, Bookable, Booking
from .serializers import BookableTypeSerializer, BookableSerializer, BookingSerializer
from rest_framework.response import Response
from src.services.BookingService import check_date_from


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
