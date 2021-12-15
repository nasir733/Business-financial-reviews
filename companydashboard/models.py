from django.db import models
from django.contrib.auth import get_user_model
from catergory.models import Catergory
User = get_user_model()
# Create your models here.


class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    catergory = models.ForeignKey(Catergory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='business_profiles/')

    def __str__(self):
        return self.name
