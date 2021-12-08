from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from .models import User
from .validators import custom_password_validator


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
            serializer.password = custom_password_validator(serializer.validated_data.get("password"))
            obj.set_passord(serializer.password)
        else:
            obj.__dict__[key] = serializer.validated_data.get(key)
    obj.save()


