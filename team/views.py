from django.shortcuts import render
from rest_framework import viewsets
from .models import Team,Participation
from .serializers import TeamSerializer,PaticipantSerializer

# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ParticipationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed or edited.
    """
    queryset = Participation.objects.all()
    serializer_class = PaticipantSerializer