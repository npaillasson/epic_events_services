# Generated by Django 3.2.9 on 2021-11-22 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='entreprise',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.CharField(choices=[(1, 'Gestion'), (2, 'Vente'), (3, 'Support')], default=None, max_length=30),
            preserve_default=False,
        ),
    ]
