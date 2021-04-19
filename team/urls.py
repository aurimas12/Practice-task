# from django.urls import path,,url
from django.urls import include,path
from django.conf.urls import url 
from team.views import *




# router.register('team1',views.TeamView)

urlpatterns = [
    path("participant/", get_participants_all),
    path("team/participant/create/", CreateParticipation.as_view()),
    path("team/", get_teams_all),
    path("team/participant/<int:pk>/", participant_by_id),
    path("team/participant/<int:pk>/delete/", participant_delete),

   
    path("team/team/create/", CreateTeam.as_view()),
    
    path("student/create/", CreateStudent.as_view()),

    # path("edit", EditMethod.as_view()),

    
   
  
    ]