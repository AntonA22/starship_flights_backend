# Generated by Django 4.2.7 on 2024-11-04 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_flight_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 4, 8, 14, 49, 582335, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]