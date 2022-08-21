from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

USER_TYPE_CHOICES = (("student", "student"), ("educator", "educator"))

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

