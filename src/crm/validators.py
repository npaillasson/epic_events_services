import re
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import User


FRENCH_PHONE_NUMBER_PATTERN = re.compile(r"^0[1-9]([ -.]?[0-9]{2}){4}$")

def phone_number_validator(phone_number):
    phone_number = phone_number.strip()
    if FRENCH_PHONE_NUMBER_PATTERN.match(phone_number):
        return phone_number
    else:
        raise ValidationError(detail="Ce numéro de téléphone n'est pas valide !")

def team_validator(id, team):
    try:
        User.objects.get(id=id, team=team)
    except ObjectDoesNotExist:
        raise ValidationError(detail=f"Erreur: Cette personne n'existe pas ou ne fait pas partie de l'equipe {team}!"
                              )

def end_date_validator(start_date, end_date):
    if start_date < end_date:
        raise ValidationError(detail ="Erreur: La date de fin de l'évènement ne peut pas être avant la date de début!")

