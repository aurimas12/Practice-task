from django.shortcuts import render
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins,viewsets
from rest_framework import status



from rest_framework import viewsets

from .models import *
from .serializers import *

class BookableTypeViewSet(viewsets.ModelViewSet):
    queryset=BookableType.objects.all()
    serializer_class= BookableTypeSerializer
