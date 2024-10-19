from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=False)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=700)
