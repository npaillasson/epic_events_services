# Generated by Django 3.2.9 on 2021-12-01 09:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0012_alter_contract_client"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="additional_information",
            field=models.TextField(
                blank=True, max_length=1000, verbose_name="information additionnelle"
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="company",
            field=models.CharField(
                blank=True, max_length=200, verbose_name="entreprise"
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="first_name",
            field=models.CharField(max_length=150, verbose_name="prénom"),
        ),
        migrations.AlterField(
            model_name="client",
            name="last_name",
            field=models.CharField(max_length=150, verbose_name="nom"),
        ),
        migrations.AlterField(
            model_name="client",
            name="phone_number",
            field=models.CharField(
                max_length=12, unique=True, verbose_name="numéro de telephone"
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="additional_information",
            field=models.TextField(
                blank=True, max_length=1000, verbose_name="information additionnelle"
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="amount",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="montant du contrat (€)",
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="signature_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="date de signature"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="additional_information",
            field=models.TextField(
                blank=True, max_length=1000, verbose_name="information additionnelle"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateTimeField(verbose_name="date de fin"),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_name",
            field=models.CharField(max_length=100, verbose_name="non de l'évènement"),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateTimeField(verbose_name="date de début"),
        ),
    ]
