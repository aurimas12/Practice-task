from django.urls import include,path
from django.conf.urls import url 
from team.views import *

urlpatterns = [
    path("team/participation_all", get_participants_all),
    path("team/participation/<int:pk>/", participant_by_id),
    path("team/participant/create", CreateParticipation.as_view()),
    path("participant/<int:pk>/update", ParticipantUpdate.as_view()),
    path("team/<int:pk>/delete/", participant_delete),
]