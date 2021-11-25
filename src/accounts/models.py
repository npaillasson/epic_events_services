from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import Group
from .validators import custom_password_validator, username_creation, assignment_of_groups, assignement_is_superuser

TEAM_CHOICES = [
    ("1", "Gestion"),
    ("2", "Vente"),
    ("3", "Support"),
]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, team):
        user = self.model(first_name=first_name,
                          email=email,
                          last_name=last_name,
                          username=username_creation(first_name=first_name, last_name=last_name),
                          team=team,
                          is_staff=True,
                          is_superuser=assignement_is_superuser(team))

        user.save()
        assignment_of_groups(team, user)
        user.set_password(custom_password_validator(password=password))
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, first_name, last_name, team):
        user = self.model(first_name=first_name,
                          email=email,
                          last_name=last_name,
                          username=username,
                          team=team,
                          is_staff=True,
                          is_superuser=True)

        user.set_password(custom_password_validator(password=password))
        user.save(using=self._db)
        return user

class User(AbstractUser):

    first_name = models.CharField('prénom', blank=False, max_length=150)
    last_name = models.CharField("Nom de famille", blank=False, max_length=150)
    email = models.EmailField(blank=False, unique=True)
    team = models.CharField("équipe", choices=TEAM_CHOICES, max_length=30)
    username = models.CharField("nom d'utilisateur", blank=True, max_length=150, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'team']


    objects = CustomUserManager()


