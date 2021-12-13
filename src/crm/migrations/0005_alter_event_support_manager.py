# Generated by Django 3.2.9 on 2021-11-27 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crm", "0004_alter_event_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="support_manager",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="support_manager",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
