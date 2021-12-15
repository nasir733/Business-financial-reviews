# Generated by Django 3.0 on 2021-12-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catergory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catergory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='catergory',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='catergory_pics'),
        ),
    ]
