from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    exclude = ('username', 'user_permissions', "password", "is_superuser", "is_staff",
               "is_active", "last_login", "date_joined")

# Register your models here.
