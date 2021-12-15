from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from .models import User
from .validators import custom_password_validator
from .custom_functions import assignement_is_superuser, assignment_of_groups


def get_user(user_id):
    if user_id == "all":
        queryset = User.objects.all()
    else:
        try:
            queryset = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise NotFound()
    return queryset


def partial_user_update(serializer, data, obj):
    for key in data.keys():
        if key == "password":
            serializer.password = custom_password_validator(
                serializer.validated_data.get("password")
            )
            obj.set_passord(serializer.password)
        if key == "team":
            obj.__dict__[key] = serializer.validated_data.get(key)
            assignment_of_groups(serializer.validated_data.get(key), obj)
            obj.is_superuser = assignement_is_superuser(serializer.validated_data.get(key))
        else:
            obj.__dict__[key] = serializer.validated_data.get(key)
    obj.save()
