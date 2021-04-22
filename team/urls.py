from django.urls import include, path
from team.views import (
    get_participants_all,
    participant_by_id,
    CreateParticipation,
    ParticipantUpdate,
    participant_delete,
)

urlpatterns = [
    path("team/participant/all", get_participants_all),
    path("team/participant/<int:pk>/", participant_by_id),
    path("team/participant/create", CreateParticipation.as_view()),
    path("team/participant/<int:pk>/update", ParticipantUpdate.as_view()),
    path("team/participant/<int:pk>/delete/", participant_delete),
]