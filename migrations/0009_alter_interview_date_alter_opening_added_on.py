# Generated by Django 5.0.6 on 2024-05-28 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_interview_date_alter_opening_added_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 28, 16, 11, 44, 575489, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='opening',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 28, 16, 11, 44, 571490, tzinfo=datetime.timezone.utc)),
        ),
    ]