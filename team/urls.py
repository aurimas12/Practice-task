from django.urls import path,include
from rest_framework import routers
from team import views

# router =routers.DefaultRouter()
# # router.register(r'team',views.TeamViewSet)
# router.register('participation',views.ParticipationViewSet.list)
# router.register('tean/12',views.ParticipationViewSet.as_view({'get':'list'}))


# router.register('team1',views.TeamView)

urlpatterns = [
    # path('', include(router.urls)),
    path("team/", views.get_teams_all),
    path("participant/", views.get_participants_all),
    path("team/participant/<str:pk>/", views.participant_by_id),
    path("team/participant/<int:pk>/delete/", views.participant_delete),
    # path("team/test-create", views.create),
  
    ]