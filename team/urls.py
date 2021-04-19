# from django.urls import path,,url
from django.urls import include,path
from django.conf.urls import url 
from team.views import *




# router.register('team1',views.TeamView)

urlpatterns = [
    # list all participants
    path("participant/get_all", get_participants_all),
    # add participant
    path("participant/create/", CreateParticipation.as_view()),
    # edit participant
    path("participant/<int:pk>/update", ParticipantUpdate.as_view()),
    # delete participant
    path("team/participant/<int:pk>/delete/", participant_delete),
    # get single participant
    path("team/participant/<int:pk>/", participant_by_id),
    

    
    
]