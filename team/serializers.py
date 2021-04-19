from rest_framework import serializers
from .models import Team,Participation,Student

class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Team
        fields=['id','members','name','url','logo']

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Participation
        fields='__all__'
    
    # def create(self,validated):
    #     Participation.objects.create(**validated_data)
    #     return Response('created')
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'