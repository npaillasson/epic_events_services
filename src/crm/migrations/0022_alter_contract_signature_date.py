# Generated by Django 3.2.9 on 2021-12-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0021_alter_contract_signature_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='signature_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date de signature'),
        ),
    ]
