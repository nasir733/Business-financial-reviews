from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
# Create your models here.

USER_TYPE_CHOICES = (
    ('Business', 'Business'),
    ('User', 'User'),
)


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=120, unique=True, blank=True, null=True)
    password = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(max_length=120, blank=True, null=True)
    user_type = models.CharField(
        max_length=120, blank=True, null=True, choices=USER_TYPE_CHOICES)
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
