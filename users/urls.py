from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import UserViewSet, UserGroupViewSet

urlpatterns = [
    path("users/all", UserViewSet.as_view({"get": "list"}), name="users-list"),
    path("users/create", UserViewSet.as_view({"post": "create"}), name="users-create"),
    path("users/group/all", UserGroupViewSet.as_view({"get": "list"})),
    path("users/create/group", UserGroupViewSet.as_view({"post": "create"})),
    path("users/<int:pk>/group", UserGroupViewSet.as_view({"get": "get_user_group"})),
]