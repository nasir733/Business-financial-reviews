# Generated by Django 3.0 on 2021-12-15 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companydashboard', '0002_auto_20211215_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
    ]
