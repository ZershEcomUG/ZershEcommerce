from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to= 'slider_imgs')
    active = models.BooleanField(default = False)

    def __str__(self):
        return self.image

class PromotionImg(models.Model):
    image = models.ImageField(upload_to= 'header_imgs')
    active = models.BooleanField(default = False)

    def __str__(self):
        return self.image        