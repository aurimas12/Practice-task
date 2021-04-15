from rest_framework import serializers
from .models import Team,Participation

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields='__all__'

class PaticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Participation
        fields='__all__'