from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .custom_functions import assignment_of_groups, assignement_is_superuser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "team", "groups", "username")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        data = self.cleaned_data
        user = get_user_model().objects.create_user(
            email=data["email"],
            password=data["password1"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            team=data["team"],
        )
        user.save()
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.

    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()

        fields = ("username",)


    def save(self, commit=True):
        user = super(CustomUserChangeForm, self).save(commit=False)
        data = self.cleaned_data
        user.is_superuser = assignement_is_superuser(data["team"])
        print(data["team"])
        assignment_of_groups(data["team"], user)
        print(user.groups.all())
        user.save()
        if commit:
            user.save()
        return user
