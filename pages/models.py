from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to= 'slider_imgs')

    def __str__(self):
        return self.image

class HeaderImg(models.Model):
    image = models.ImageField(upload_to= 'header_imgs')

    def __str__(self):
        return self.image        