from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User
from .form import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    def has_view_permission(self, request, obj=None):
        return True

    readonly_fields = ("username",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "team",
        "email",
    )
    list_filter = ()
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "team",
                    "groups",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "team",
                    "password1",
                    "password2",
                    "groups",
                )
            },
        ),
    )
    search_fields = ("username", "first_name", "last_name", "team", "email")
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
