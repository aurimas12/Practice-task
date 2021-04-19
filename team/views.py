from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Team,Participation,Student
from .serializers import TeamSerializer,ParticipantSerializer,StudentSerializer
from rest_framework.response import Response

from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.views import APIView

from rest_framework import status, generics, mixins,viewsets
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

# TODO
"""
GET/POST/PUT/DELETE team api (/team/{team_id}/participant/{participant_id})
 - list all participants (if no participant id provided)        +
 - get singe participant                                        +
 - add participant (underthehood, calls django create user)
 - edit participant (except password)
 - delete participant (user stays, just mapping deleted)        +   
 """

# list all teams 
@api_view(["GET"])
def get_teams_all(req):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)

# list all participants  
@api_view(["GET"])    
def get_participants_all(req):
    teams = Participation.objects.all()
    serializer = ParticipantSerializer(teams, many=True)
    return Response(serializer.data)

# get single participant
@api_view(["GET"])
def participant_by_id(req,pk):
    participant = Participation.objects.get(id=pk)
    serializer = ParticipantSerializer(participant, many=False)
    return Response(serializer.data)

# delete participant 
@api_view(['DELETE'])
def participant_delete(req,pk): 
    query = Participation.objects.get(id=pk)
    query.delete()
    return Response('deleted')

# Create participation
class CreateParticipation(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
):

    serializer_class = ParticipantSerializer
    
    def post(self, request):

        return self.create(request)

# Create team
class CreateTeam(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
):

    serializer_class = TeamSerializer

    def post(self, request):
        
        return self.create(request)


class CreateStudent(generics.GenericAPIView,
    mixins.CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
    print('create func start')
    def post(self, request):
        
        return self.create(request)

