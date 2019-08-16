from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    role = models.IntegerField(default=2)
    
    def __str__(self):
        return self.email