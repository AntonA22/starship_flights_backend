# Generated by Django 4.2.7 on 2024-10-15 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_flight_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 15, 6, 29, 50, 644775, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]