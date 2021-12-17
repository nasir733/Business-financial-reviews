from django.db import models
from django.contrib.auth import get_user_model
from catergory.models import Catergory
User = get_user_model()
# Create your models here.


class BusinessProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=300, blank=True, null=True)
    website = models.URLField(
        max_length=200, default=' ', blank=True, null=True)
    facebook = models.URLField(
        max_length=200, default=' ', blank=True, null=True)
    twitter = models.URLField(
        max_length=200, default=' ', blank=True, null=True)
    instagram = models.URLField(
        max_length=200, default=' ', blank=True, null=True)

    catergory = models.ForeignKey(Catergory, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='business_profiles/', default='default2.png')
    avg_rating = models.FloatField(default=0)

    class Meta:
        ordering = ['-avg_rating']

    def __str__(self):
        return self.name
