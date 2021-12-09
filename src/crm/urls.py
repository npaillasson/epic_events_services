from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import DisplayClient

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
            }
        )
    )
]