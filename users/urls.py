from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import UserViewSet

urlpatterns = [
    path("user1/all", UserViewSet.as_view({"get": "list"})),
    path("user1/create", UserViewSet.as_view({"post": "create"})),
]