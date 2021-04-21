from django.urls import include,path
from booking.views import BookableTypeViewSet,BookableViewSet

urlpatterns=[
    # BookableType
    path('bookable-type/all', BookableTypeViewSet.as_view({'get': 'list'}), name='bookable-type'),
    path('bookable-type/create', BookableTypeViewSet.as_view({'post': 'create'}), name='bookable-type'),
    # Bookable
    path('bookable/all', BookableViewSet.as_view({'get': 'list'}), name='bookable'),
    path('bookable/edit/<int:pk>', BookableViewSet.as_view({'put': 'update'}), name='bookable'),
    path('bookable/create', BookableViewSet.as_view({'post': 'create'}), name='bookable'),
    path('bookable/get/<int:pk>', BookableViewSet.as_view({'get':'list'}), name='bookable'),
    path('bookable/delete/<int:pk>', BookableViewSet.as_view({'delete': 'destroy'}), name='bookable'),
    # Booking
    ]