from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, TEAM_CHOICES


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'team')

    def save(self, commit=True):
        print("SAVEMODEL")
        data = self.cleaned_data
        user = super(CustomUserCreationForm, self).save(commit=False)
        user = get_user_model().objects.create_user(email=data["email"],password=data["password1"],
                                                    first_name=data["first_name"],last_name=data["last_name"],
                                                    team=data["team"])
        user.save()
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')


