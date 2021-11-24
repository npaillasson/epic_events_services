from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    exclude = ('username', 'groups')

# Register your models here.
