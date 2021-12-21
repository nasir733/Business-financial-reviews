from django.db import models

# Create your models here.


class Catergory(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(
        upload_to='catergory_pics', blank=True, null=True)

    def __str__(self):
        return self.name
