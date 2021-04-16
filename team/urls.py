from django.urls import path,include
from rest_framework import routers
from team.views import *

# router =routers.DefaultRouter()
# # router.register(r'team',views.TeamViewSet)
# router.register('participation',views.ParticipationViewSet.list)
# router.register('tean/12',views.ParticipationViewSet.as_view({'get':'list'}))


# router.register('team1',views.TeamView)

urlpatterns = [
    # path('', include(router.urls)),
    path("team/", get_teams_all),
    path("participant/", get_participants_all),
    path("team/participant/<str:pk>/", participant_by_id),
    path("team/participant/<int:pk>/delete/", participant_delete),
    path(r"team/participant/create/", AddParticipant.as_view()),
    # path("team/test-create", views.CreateReservation.as_view()),
    ]