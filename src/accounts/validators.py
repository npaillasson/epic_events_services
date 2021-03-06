from django.core import exceptions
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


def has_not_number(chaine):
    if not chaine.isalpha():
        raise exceptions.ValidationError(
            f"Ce champ ne doit contenir que des lettres (pas de caractères spéciaux, ou chiffres)"
        )
