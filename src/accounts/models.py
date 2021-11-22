from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TEAM_CHOICES = [
        (1, "Gestion"),
        (2, "Vente"),
        (3, "Support"),
    ]


    first_name = models.CharField(blank=False, max_length=150)
    last_name = models.CharField(blank=False, max_length=150)
    email = models.EmailField(blank=False, unique=True)
    team = models.CharField(choices=TEAM_CHOICES)
