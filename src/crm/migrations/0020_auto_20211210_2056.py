# Generated by Django 3.2.9 on 2021-12-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_alter_contract_signature_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pré-contrat',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('crm.contract',),
        ),
        migrations.AlterField(
            model_name='contract',
            name='signature_date',
            field=models.DateTimeField(blank=True, default=None, verbose_name='date de signature'),
        ),
    ]