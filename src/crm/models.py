import datetime
from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator
from rest_framework.exceptions import ValidationError
from .validators import (
    is_support_validator,
    api_team_validator,
    end_date_validator,
    phone_number_validator,
    api_end_date_validator,
    is_sale_validator,
    api_phone_number_validator,
    api_contract_validator,
    api_client_validator,
    is_client_validator,
    is_signed_validator,
)

STATUS_CHOICES = [
    ("0", "Annulé"),
    ("1", "Programmé"),
    ("2", "En cours de préparation"),
    ("3", "Terminé"),
]


class Client(models.Model):
    first_name = models.CharField("prénom", blank=False, max_length=150)
    last_name = models.CharField("nom", blank=False, max_length=150)
    company = models.CharField("entreprise", blank=True, max_length=200)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.CharField(
        "numéro de telephone",
        blank=False,
        unique=True,
        max_length=12,
        validators=[phone_number_validator],
    )
    additional_information = models.TextField(
        "information additionnelle", blank=True, max_length=1000
    )
    client_manager = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name="responsable commercial",
        related_name="client_manager",
        validators=[is_sale_validator],
    )
    is_client = models.BooleanField(
        "Convertir le prospect en client", blank=False, default=False
    )
    time_created = models.DateTimeField("créer le", auto_now_add=True)
    time_changed = models.DateTimeField("dernière modification", auto_now=True)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        api_phone_number_validator(self.phone_number)
        api_team_validator(self.client_manager, "2")
        super().save()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = f"{verbose_name}s"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contract(models.Model):
    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
        related_name="client",
        validators=[is_client_validator],
    )
    signature_date = models.DateTimeField("date de signature", blank=True, null=True)
    amount = models.IntegerField(
        "montant du contrat (€)", blank=False, validators=[MinValueValidator(0)]
    )
    additional_information = models.TextField(
        "information additionnelle", blank=True, max_length=1000
    )
    is_signed = models.BooleanField(
        "convertir le contrat en contrat signé", blank=False, default=False
    )
    time_created = models.DateTimeField("créer le", auto_now_add=True)
    time_changed = models.DateTimeField("dernière modification", auto_now=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.id:
            if not Contract.objects.get(id=self.id).is_signed and self.is_signed:
                self.signature_date = datetime.datetime.now()
                api_client_validator(self.client)
                return super().save()
            if Contract.objects.get(id=self.id).is_signed and not self.is_signed:
                raise ValidationError(
                    detail={
                        "is_signed": "Erreur! Une fois signé un contrat ne peut pas être invalidé"
                    }
                )
        elif not self.id:
            if self.is_signed:
                self.signature_date = datetime.datetime.now()
                api_client_validator(self.client)
                return super().save()
        api_client_validator(self.client)
        return super().save()

    class Meta:
        unique_together = ("id", "client")
        verbose_name = "Contrat"
        verbose_name_plural = f"{verbose_name}s"

    def __str__(self):
        return f"Contrat n° {self.pk}"


class Event(models.Model):

    contract = models.OneToOneField(
        blank=False,
        to=Contract,
        on_delete=models.CASCADE,
        related_name="contract",
        validators=[is_signed_validator],
    )
    support_manager = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        related_name="support_manager",
        validators=[is_support_validator],
    )
    event_name = models.CharField(
        "nom de l'évènement",
        blank=False,
        max_length=100,
    )
    start_date = models.DateTimeField("date de début", blank=False)
    end_date = models.DateTimeField("date de fin", blank=False)
    additional_information = models.TextField(
        "information additionnelle", blank=True, max_length=1000
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=30)
    time_created = models.DateTimeField("créer le", auto_now_add=True)
    time_changed = models.DateTimeField("dernière modification", auto_now=True)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        api_team_validator(value=self.support_manager, group="3")
        api_end_date_validator(self.start_date, self.end_date)
        api_contract_validator(self.contract)
        super().save()

    def clean(self):
        end_date_validator(self.start_date, self.end_date)

    class Meta:
        verbose_name = "Évènement"
        verbose_name_plural = f"{verbose_name}s"

    def __str__(self):
        return f"{self.event_name}"
