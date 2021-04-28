from .models import Team, Participation
from .serializers import TeamSerializer, ParticipantSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, viewsets
from src.services.BookableTypeLimitService import bookable_request_save_data

# list all participants
@api_view(["GET"])
def get_participants_all(req):
    participants = Participation.objects.all()
    serializer = ParticipantSerializer(participants, many=True)
    return Response(serializer.data)


# get single participant in team
@api_view(["GET"])
def participant_by_id(req, pk):
    participant = Participation.objects.get(id=pk)
    serializer = ParticipantSerializer(participant, many=False)
    return Response(serializer.data)


from src.services.BookableTypeLimitService import get_auth_user_name

# create participant
class CreateParticipation(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
):
    serializer_class = ParticipantSerializer

    def post(self, request):
        print(get_auth_user_name(request))
        print(get_auth_user_name(request).id)
        return self.create(request)


# delete participant
@api_view(["DELETE"])
def participant_delete(req, pk):
    query = Participation.objects.get(id=pk)
    query.delete()
    return Response("deleted")


# patricipant update
class ParticipantUpdate(generics.UpdateAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participation.objects.all()
