from django.shortcuts import render
from .models import Team,Participation
from .serializers import TeamSerializer,ParticipantSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins,viewsets

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
class CreateParticipation(generics.GenericAPIView,mixins.CreateModelMixin,):
    serializer_class = ParticipantSerializer
    def post(self, request):
        return self.create(request)

# patricipant update
class ParticipantUpdate(generics.UpdateAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participation.objects.all()