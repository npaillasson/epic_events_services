from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User
from .form import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("username", 'first_name', 'last_name', 'team', 'email',)
    list_filter = ()
    fieldsets = ((None,{"fields":('username', 'first_name', 'last_name', 'email', 'team', 'groups')}),)
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = ((None,{"fields":('first_name', 'last_name', 'email', 'team', 'password1', 'password2', 'groups')}),)
    search_fields = ("username", 'first_name', 'last_name', 'team', 'email')
    ordering = ('email',)
    filter_horizontal = ()

#@admin.register(User)
#class MyUser(admin.ModelAdmin):
#    model = get_user_model()
#    form = CustomUserCreationForm


#    def save_model(self, request, obj, form, change):
#        data = form.cleaned_data
##        User(email=data["email"],password=data["password1"],
#            first_name=data["first_name"],last_name=data["last_name"],team=data["team"])
#        User.save()
#       super().save_model(request, obj, form, change)

# Register your models here.

admin.site.register(User, UserAdmin)
