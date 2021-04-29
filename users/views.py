from .models import NewUser
from .serializers import NewUserSerializer
from rest_framework.response import Response

from rest_framework import viewsets


class NewUserViewSet(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer