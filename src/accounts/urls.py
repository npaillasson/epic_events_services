from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserCreate, DisplayUser

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "users/add-user/",
        UserCreate.as_view(
            {
                "post": "create",
            }
        ),
        name="new_account",
    ),
    path(
        "users/<int:pk>/",
        DisplayUser.as_view(
            {
                "get": "retrieve",
                "delete": "destroy",
                "patch": "update",
            }
        ),
        name="user_details",
    ),
    path(
        "users/",
        DisplayUser.as_view(
            {
                "get": "list",
            }
        ),
        name="users_list",
    ),
]
