from .models import Team, Participation
from .serializers import TeamSerializer, ParticipantSerializer
from rest_framework.response import Response

from rest_framework import viewsets


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipantSerializer

