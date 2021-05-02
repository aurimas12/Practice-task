from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserGroupSerializer, UserSerializer
from src.services.BookableTypeLimitService import BookableTypeLimitService
from django.contrib.auth.models import User
from rest_framework.decorators import action
from booking.models import Bookable
from .models import UserGroup


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    @action(detail=True, methods=["get"])
    def get_user_group(self, request, pk=None):
        user = UserGroup.objects.get(user_id=pk)
        serializer = UserGroupSerializer(user)
        return Response(serializer.data)