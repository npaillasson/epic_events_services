# Generated by Django 3.2.9 on 2021-11-29 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0007_alter_event_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="contract",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contract",
                to="crm.contract",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="event",
            unique_together=set(),
        ),
    ]
