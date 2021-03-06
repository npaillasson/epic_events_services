# Generated by Django 3.2.9 on 2021-12-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0013_auto_20211201_1048"),
    ]

    operations = [
        migrations.CreateModel(
            name="prospect",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("crm.client",),
        ),
        migrations.AddField(
            model_name="client",
            name="is_client",
            field=models.BooleanField(default=False, verbose_name="prospect"),
        ),
    ]
