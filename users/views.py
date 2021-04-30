from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import CreateUserSerializer
from src.services.BookableTypeLimitService import BookableTypeLimitService
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request):

        serializer = CreateUserSerializer(data=request.data)
        return BookableTypeLimitService.request_save_data(serializer, request)
