from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    jetons = models.IntegerField(default=0)


