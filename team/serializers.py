from rest_framework import serializers
from .models import Team, Participation, Venue


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "members", "name", "url", "logo"]


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = "__all__"


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = "__all__"
