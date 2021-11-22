import re
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError


FRENCH_PHONE_NUMBER_PATTERN = re.compile(r"^0[1-9]([ -.]?[0-9]{2}){4}$")

def phone_number_validator(phone_number):
    phone_number = phone_number.strip()
    if FRENCH_PHONE_NUMBER_PATTERN.match(phone_number):
        return phone_number
    else:
        raise ValidationError(detail="Ce numéro de téléphone n'est pas valide !")

def custom_password_validator(password):
    try:
        validate_password(password)
    except exceptions.ValidationError as exception_to_return:
        exception_to_return = ", ".join(exception_to_return)
        detail = {"password": "{}".format(exception_to_return)}
        raise ValidationError(detail=detail)
    else:
        return password