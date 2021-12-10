# Generated by Django 3.2.9 on 2021-12-09 17:38

import crm.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0017_client_client_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='time_changed',
            field=models.DateTimeField(auto_now=True, verbose_name='dernière modification'),
        ),
        migrations.AddField(
            model_name='client',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='créer le'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='is_signed',
            field=models.BooleanField(default=False, verbose_name='convertir le contrat en contrat signé'),
        ),
        migrations.AddField(
            model_name='contract',
            name='time_changed',
            field=models.DateTimeField(auto_now=True, verbose_name='dernière modification'),
        ),
        migrations.AddField(
            model_name='contract',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='créer le'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time_changed',
            field=models.DateTimeField(auto_now=True, verbose_name='dernière modification'),
        ),
        migrations.AddField(
            model_name='event',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='créer le'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='client_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_manager', to=settings.AUTH_USER_MODEL, validators=[crm.validators.is_sale_validator], verbose_name='responsable commercial'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True, validators=[crm.validators.phone_number_validator], verbose_name='numéro de telephone'),
        ),
    ]
