from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=30, blank=True)
    is_verified = models.BooleanField(default=False)



