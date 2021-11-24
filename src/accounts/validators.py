from django.core import exceptions
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError

def custom_password_validator(password):
    try:
        validate_password(password)
    except exceptions.ValidationError as exception_to_return:
        exception_to_return = ", ".join(exception_to_return)
        detail = {"password": "{}".format(exception_to_return)}
        raise ValidationError(detail=detail)
    else:
        return password

def username_creation(first_name, last_name):
    return last_name + first_name[:1]

def assignement_is_superuser(team):
    match team:
        case "1":
            return True
        case _:
            return False


def assignment_of_groups(team, user):
    match team:
        case "1":
            return None
        case "2":
            Group.objects.get(name="vente").user_set.add(user)
        case "3":
            Group.objects.get(name="support").user_set.add(user)