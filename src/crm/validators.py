import re
import time
from django.core import exceptions
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import User

FRENCH_PHONE_NUMBER_PATTERN = re.compile(r"^0[1-9]([ -.]?[0-9]{2}){4}$")

def phone_number_validator(phone_number):
    phone_number = phone_number.strip()
    if FRENCH_PHONE_NUMBER_PATTERN.match(phone_number):
        return phone_number
    else:
        raise exceptions.ValidationError("Ce numéro de téléphone n'est pas valide !")

def api_phone_number_validator(value):
    try:
        phone_number_validator(value)
    except exceptions.ValidationError as exception_to_return:
        exception_to_return = ", ".join(exception_to_return)
        detail = {"phone_number": "{}".format(exception_to_return)}
        raise ValidationError(detail=detail)
    else:
        return value


def is_in_group(value, group):
    try:
        User.objects.get(id=value, team=group)
    except ObjectDoesNotExist:
        raise exceptions.ValidationError("Erreur: Cette personne n'existe pas ou "
                                         "ne fait pas partie de la bonne équipe!")

def is_support_validator(value):
    is_in_group(value, "3")

def is_sale_validator(value):
    is_in_group(value, "2")

def api_team_validator(value, group):
    try:
        is_in_group(value, group)
    except exceptions.ValidationError as exception_to_return:
        exception_to_return = ", ".join(exception_to_return)
        detail = {"team": "{}".format(exception_to_return)}
        raise ValidationError(detail=detail)
    else:
        return value


def api_end_date_validator(start_date, end_date):
    if start_date > end_date:
        raise ValidationError(detail="Erreur: La date de fin de l'évènement ne peut pas être avant la date de début!")

def end_date_validator(start_date, end_date):
    if start_date > end_date:
        raise exceptions.ValidationError("Erreur: La date de fin de l'évènement ne peut pas être avant la date de début!")