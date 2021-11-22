from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    first_name = models.CharField(blank=False, max_length=150)
    last_name = models.CharField(blank=False, max_length=150)
    entreprise = models.CharField(blank=True, max_length=200)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.CharField(blank=False, unique=True, max_length=12)
