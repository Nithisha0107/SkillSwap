from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


def upload_to(instance, filename):
    return f'images/{filename}'

class User(AbstractUser):
    phone_number = PhoneNumberField()
    qualification = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    occupation = models.CharField(max_length=250, null=True, blank=True)
    profile_picture = models.ImageField(upload_to=upload_to, null=True, blank=True)
