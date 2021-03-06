from rest_framework import serializers
from .models import Team, Participation


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "members", "name", "url", "logo"]


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = "__all__"
