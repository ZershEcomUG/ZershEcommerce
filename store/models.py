from django.db import models
from user.models import *
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='cat_imgs')
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #   return reverse('subcat_detail', args=[str(self.id)])    

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    image = models.ImageField(upload_to='pdt_imgs/')
    sku = models.IntegerField()
    available = models.BooleanField(default=True)
    discount = models.IntegerField(default = 0)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('pdt_detail', args=[str(self.id)])

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', args= [str(self.id)] )    


class Order(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.customer.username


class OrderItem(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False, null=True, blank=False)    
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} "


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


