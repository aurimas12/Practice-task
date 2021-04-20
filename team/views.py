from django.shortcuts import render
from .models import Team,Participation
from .serializers import TeamSerializer,ParticipantSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins,viewsets
from rest_framework import status

# list all participants  
@api_view(["GET"])    
def get_participants_all(req):
    participants = Participation.objects.all()
    serializer = ParticipantSerializer(participants, many=True)
    return Response(serializer.data)

# get single participant in team
@api_view(["GET"])
def participant_by_id(req,pk):
    participant = Participation.objects.get(id=pk)
    serializer = ParticipantSerializer(participant, many=False)
    return Response(serializer.data)

# create participant
class CreateParticipation(generics.GenericAPIView,mixins.CreateModelMixin,):
    serializer_class = ParticipantSerializer
    def post(self, request):
        return self.create(request)

# delete participant 
@api_view(['DELETE'])
def participant_delete(req,pk): 
    query = Participation.objects.get(id=pk)
    query.delete()
    return Response('deleted')

# patricipant update
class ParticipantUpdate(generics.UpdateAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participation.objects.all()
