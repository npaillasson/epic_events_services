# Generated by Django 3.2.9 on 2021-11-30 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20211129_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='crm.client'),
        ),
    ]
