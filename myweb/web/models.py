from django.contrib.auth.models import AbstractUser
from django.db import models

class Contacts(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    Telephone = models.CharField(max_length=30)
    message = models.CharField(max_length=30)
