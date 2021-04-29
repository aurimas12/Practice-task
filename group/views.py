from django.shortcuts import render
from .models import Group
from .serializers import GroupSerializer
from rest_framework.response import Response
from rest_framework import viewsets


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer