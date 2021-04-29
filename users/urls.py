from django.urls import include, path

# from users.views import NewUserViewSet
from users.views import NewUserViewSet

urlpatterns = [
    # Team
    path("new-user/all", NewUserViewSet.as_view({"get": "list"})),
    path("new-user/create", NewUserViewSet.as_view({"post": "create"})),
    # path("team/delete/<int:pk>", TeamViewSet.as_view({"delete": "destroy"})),
    # # Participant
    # path("participant/all", TeamViewSet.as_view({"get": "list"})),
    # path("participant/create", TeamViewSet.as_view({"post": "create"})),
    # path("participant/delete/<int:pk>", TeamViewSet.as_view({"delete": "destroy"})),
    # path("participant/edit/<int:pk>", ParticipantViewSet.as_view({"put": "update"})),
]