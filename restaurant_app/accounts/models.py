from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username