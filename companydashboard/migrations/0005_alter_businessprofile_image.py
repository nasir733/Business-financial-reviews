# Generated by Django 3.2.9 on 2021-12-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companydashboard', '0004_auto_20211216_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='image',
            field=models.ImageField(default='default2.png', upload_to='business_profiles/'),
        ),
    ]
