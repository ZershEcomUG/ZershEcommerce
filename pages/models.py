from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to= 'slider_imgs')
    active = models.BooleanField(default = False)

    def __str__(self):
        return str(self.image)

class PromotionImg(models.Model):
    image = models.ImageField(upload_to= 'header_imgs')
    active = models.BooleanField(default = False)

    def __str__(self):
        return str(self.image)    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.name            