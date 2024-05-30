# Generated by Django 5.0.6 on 2024-05-28 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_profile_alter_opening_added_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'interview',
            },
        ),
        migrations.AlterField(
            model_name='opening',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 28, 13, 20, 4, 20326, tzinfo=datetime.timezone.utc)),
        ),
    ]