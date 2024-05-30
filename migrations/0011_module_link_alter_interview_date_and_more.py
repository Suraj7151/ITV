# Generated by Django 5.0.6 on 2024-05-28 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_alter_interview_date_alter_opening_added_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 28, 20, 56, 43, 943314, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='opening',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 28, 20, 56, 43, 939314, tzinfo=datetime.timezone.utc)),
        ),
    ]