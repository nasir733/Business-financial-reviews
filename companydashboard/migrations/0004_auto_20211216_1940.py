# Generated by Django 3.2.9 on 2021-12-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companydashboard', '0003_businessprofile_avg_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessprofile',
            options={'ordering': ['-avg_rating']},
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
