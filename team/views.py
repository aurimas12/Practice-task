from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Team,Participation
from .serializers import TeamSerializer,ParticipantSerializer
from rest_framework.response import Response

from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.views import APIView
# TODO
"""
GET/POST/PUT/DELETE team api (/team/{team_id}/participant/{participant_id})
 - list all participants (if no participant id provided)        +
 - get singe participant                                        +
 - add participant (underthehood, calls django create user)
 - edit participant (except password)
 - delete participant (user stays, just mapping deleted)
 """

# list all participants (if no participant id provided)
@api_view(["GET"])
def get_teams_all(req):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)

# get single participant
@api_view(["GET"])
def participant_by_id(req,pk):
    participant = Participation.objects.get(id=pk)
    serializer = ParticipantSerializer(participant, many=False)
    return Response(serializer.data)


