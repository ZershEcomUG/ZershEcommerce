from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    pass


class Customer(CustomUser):

    address = models.CharField(max_length=180)

    def __str__(self):
        return self.username


class Seller(CustomUser):

    store_name = models.CharField(max_length=120)
    address = models.CharField(max_length=180)

    def __str__(self):
        return self.username
