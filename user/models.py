from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.


class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    phone = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return  reverse('user_dash', args=[str(self.id)])


class Seller(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    store_name = models.CharField(max_length=120)
    address = models.CharField(max_length=180)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField( max_length=180, blank=True, null=True )
    

    def __str__(self):
        return self.store_name
