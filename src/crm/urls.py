from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import DisplayClient, DisplayContract, DisplayEvent

urlpatterns = [
    path(
        "clients/",
        DisplayClient.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="clients",
    ),
    path(
        "clients/<int:pk>/",
        DisplayClient.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "delete": "destroy",
            }
        )
    ),
    path(
        "contracts/",
        DisplayContract.as_view(
            {
                "get": "list",
                "post": "create",
            }
        )
    ),
    path(
        "contracts/<int:pk>/",
        DisplayContract.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "delete": "destroy",
            }
        )
    ),
    path(
        "events/",
        DisplayEvent.as_view(
            {
                "get": "list",
                "post": "create",
            }
        )
    ),
    path(
        "events/<int:pk>/",
        DisplayEvent.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "delete": "destroy",
            }
        )
    ),
]