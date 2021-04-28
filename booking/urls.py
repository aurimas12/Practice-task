from django.urls import include, path
from booking.views import (
    BookableTypeViewSet,
    BookableViewSet,
    BookingViewSet,
    BookableTypeLimitViewSet,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Authentication
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # BookableTypeLimit
    path(
        "bookable-type-limit/all",
        BookableTypeLimitViewSet.as_view({"get": "list"}),
        name="bookable-type",
    ),
    path(
        "bookable-type-limit/create",
        BookableTypeLimitViewSet.as_view({"post": "create"}),
        name="bookable-type",
    ),
    path(
        "bookable-type-limit/all/edit/<int:pk>",
        BookableTypeLimitViewSet.as_view({"put": "update"}),
        name="bookable-type",
    ),
    # BookableType
    path(
        "bookable-type/all",
        BookableTypeViewSet.as_view({"get": "list"}),
        name="bookable-type",
    ),
    path(
        "bookable-type/create",
        BookableTypeViewSet.as_view({"post": "create"}),
        name="bookable-type",
    ),
    # Bookable
    path("bookable/all", BookableViewSet.as_view({"get": "list"}), name="bookable"),
    path(
        "bookable/edit/<int:pk>",
        BookableViewSet.as_view({"put": "update"}),
        name="bookable",
    ),
    path(
        "bookable/create", BookableViewSet.as_view({"post": "create"}), name="bookable"
    ),
    path(
        "bookable/get/<int:pk>",
        BookableViewSet.as_view({"get": "list"}),
        name="bookable",
    ),
    path(
        "bookable/delete/<int:pk>",
        BookableViewSet.as_view({"delete": "destroy"}),
        name="bookable",
    ),
    # Booking
    path("booking/all", BookingViewSet.as_view({"get": "list"}), name="booking"),
    path(
        "booking/create",
        BookingViewSet.as_view({"post": "create"}),
        name="booking_create",
    ),
    path(
        "booking/delete/<int:pk>",
        BookingViewSet.as_view({"delete": "destroy"}),
        name="bookable",
    ),
]
