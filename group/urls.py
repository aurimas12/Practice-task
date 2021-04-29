from django.urls import include, path

from .views import GroupViewSet


urlpatterns = [
    path("group/all", GroupViewSet.as_view({"get": "list"})),
    path("group/create", GroupViewSet.as_view({"post": "create"})),
]
