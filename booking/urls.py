from django.urls import include,path
from booking.views import BookableTypeViewSet



urlpatterns=[
    path('bookable-type/all', BookableTypeViewSet.as_view({'get': 'list'}), name='bookable-type'),
    path('bookable-type/create', BookableTypeViewSet.as_view({'post': 'create'}), name='bookable-type'),
    ]