from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator
from .validators import team_validator, end_date_validator, phone_number_validator
class Client(models.Model):
    first_name = models.CharField(blank=False, max_length=150)
    last_name = models.CharField(blank=False, max_length=150)
    company = models.CharField(blank=True, max_length=200)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.CharField(blank=False, unique=True, max_length=12)
    additional_information = models.CharField(blank=True, max_length= 1000)
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None,):
        self.phone_number = phone_number_validator(self.phone_number)
        super().save()

class Contract(models.Model):
    client = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="client")
    signature_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    additional_information = models.CharField(blank=True, max_length=1000)

class Events(models.Model):

    STATUS_CHOICES = [
        (0, "Annulé"),
        (1, "Programmé"),
        (2, "En cours de préparation"),
        (3, "Terminé"),
    ]

    contract = models.ForeignKey(blank=False, to=Contract, on_delete=models.CASCADE, related_name="contract")
    support_manager = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False)
    event_name = models.CharField(blank=False, max_length=100)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    additional_information = models.CharField(blank=True, max_length=1000)
    status = models.CharField(choices=STATUS_CHOICES, max_length=30)
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None,):
        team_validator(id=self.support_manager, team=3)
        end_date_validator(self.start_date, self.end_date)
        super().save()

    class Meta:
        unique_together = ('id', 'contract')