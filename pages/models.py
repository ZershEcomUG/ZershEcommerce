from django.db import models
from store.models import Category, SubCategory

# Create your models here.

class Slider(models.Model):
    image_1920x358 = models.ImageField(upload_to= 'slider_imgs')
    active = models.BooleanField(default = False)
    heading =  models.CharField(max_length=200, blank=True, null=True)
    description =  models.CharField(max_length=200, blank=True, null=True)
    description2 =  models.CharField(max_length=200, blank=True, null=True)
    associated_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    associated_subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    point_to_category = models.BooleanField(default = False, blank=True, null=True)
    point_to_subcateory = models.BooleanField(default = False, blank=True, null=True)

    def __str__(self):
        return str(self.image)

class PromotionImg(models.Model):
    image_379x188 = models.ImageField(upload_to= 'header_imgs')
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

class Ad(models.Model):
    name = models.CharField(max_length=200)  
    image1920x80 = models.ImageField(upload_to= 'ad_imgs') 
    discount_offer =  models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200) 
    description2 = models.CharField(max_length=200) 
    active = models.BooleanField(default = False)

    def __str__(self):
        return self.name 