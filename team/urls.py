from django.urls import path,include
from rest_framework import routers
from team import views

router =routers.DefaultRouter()
router.register(r'team',views.TeamViewSet)
router.register(r'participation',views.ParticipationViewSet)
urlpatterns = [
    path('', include(router.urls)),

    ]