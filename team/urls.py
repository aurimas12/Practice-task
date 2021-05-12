from django.urls import include, path
from team.views import TeamViewSet, ParticipantViewSet, VenueViewSet


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
    # Venue
    path("venue/all", VenueViewSet.as_view({"get": "list"})),
    path("venue/create", VenueViewSet.as_view({"post": "create"})),
    path("venue/delete/<int:pk>", VenueViewSet.as_view({"delete": "destroy"})),
    path("venue/edit/<int:pk>", VenueViewSet.as_view({"put": "update"})),
]