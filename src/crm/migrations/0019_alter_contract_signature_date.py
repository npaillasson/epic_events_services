# Generated by Django 3.2.9 on 2021-12-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_auto_20211209_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='signature_date',
            field=models.DateTimeField(default=None, verbose_name='date de signature'),
        ),
    ]