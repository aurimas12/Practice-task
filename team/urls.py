from django.urls import include, path
from team.views import TeamViewSet, ParticipantViewSet


urlpatterns = [
    # Team
    path("team", TeamViewSet.as_view({"get": "list"}), name="team"),
    path("team/create", TeamViewSet.as_view({"post": "create"})),
    path("team/delete/<int:pk>", TeamViewSet.as_view({"delete": "destroy"})),
    # Participant
    path("participant/all", TeamViewSet.as_view({"get": "list"})),
    path("participant/create", TeamViewSet.as_view({"post": "create"})),
    path("participant/delete/<int:pk>", TeamViewSet.as_view({"delete": "destroy"})),
    path("participant/edit/<int:pk>", ParticipantViewSet.as_view({"put": "update"})),
]