# Generated by Django 3.2.9 on 2021-11-26 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_rename_events_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Contrat', 'verbose_name_plural': 'Contrats'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Evènement', 'verbose_name_plural': 'Evènements'},
        ),
    ]