from django.db import models
from django.contrib.auth import get_user_model
from catergory.models import Catergory
User = get_user_model()
# Create your models here.


class BusinessProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    website = models.URLField(
        max_length=200, default=' ', blank=True, null=True)
    facebook = models.URLField(
        max_length=200, default=' ', blank=True, null=True)
    twitter = models.URLField(
        max_length=200, default=' ', blank=True, null=True)
    instagram = models.URLField(
        max_length=200, default=' ', blank=True, null=True)

    catergory = models.ForeignKey(
        Catergory, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(
        upload_to='business_profiles/', default='default2.png', null=True, blank=True)
    avg_rating = models.FloatField(default=0, null=True, blank=True)
    employee_count = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    score = models.CharField(max_length=100, blank=True, null=True)
    sales = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-avg_rating']

    def __str__(self):
        return self.name
