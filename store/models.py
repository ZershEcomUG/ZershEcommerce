from django.db import models
from user.models import CustomUser, Seller
from django.urls import reverse
from model_utils import Choices


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120)
    image_263x629 = models.ImageField(upload_to='cat_imgs')
    image_263x629_2 = models.ImageField(upload_to='cat_imgs')
    image_263x629_3 = models.ImageField(upload_to='cat_imgs')
    image_mobi_770x331 = models.ImageField(upload_to='cat_imgs/mobi', blank=True, null=True)
    img_array = [image_263x629, image_263x629_2, image_263x629_3]
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
    image_182x182 = models.ImageField(upload_to='pdt_imgs/')
    image_1200x1200 = models.ImageField(upload_to='pdt_imgs/alt_imgs/')
    image_600x600 = models.ImageField(upload_to='pdt_imgs/alt_imgs/')
    image_600x600_2 = models.ImageField(upload_to='pdt_imgs/alt_imgs/')
    image_300x300 = models.ImageField(upload_to='pdt_imgs/alt_imgs/')
    img_array = [image_1200x1200, image_600x600, image_600x600_2]
    sku = models.IntegerField()
    available = models.BooleanField(default=True)
    discount = models.IntegerField(default = 0)
    description = models.CharField(max_length=120, blank=True, null=True)
    brand = models.CharField(max_length=120, blank=True, null=True)
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
    billing_details = models.ForeignKey( 'BillingDetails', on_delete = models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey( 'Payment', on_delete = models.SET_NULL, blank=True, null=True)
    delivery = models.ForeignKey( 'Delivery', on_delete = models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.customer.username

    def total_price(self):
        total = 0
        for orderitem in self.orderitem_set.all():
            total += orderitem.get_final_price()
        return total   

    def total_price_deliv(self):
        total = self.total_price() + 5000
        return total

    def total_price_deliv_pickup(self):
        total = self.total_price() + 2000
        return total         

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

    def  get_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_item_discount_price(self):
        discount_price = self.product.price - (self.product.discount/100 * self.product.price)      
        return self.quantity * discount_price

    def get_final_price(self):
        if self.product.discount > 0:
            return self.get_total_item_discount_price()
        return  self.get_total_item_price()

class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class BillingDetails(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    phone = models.IntegerField()
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    building_apartment_name = models.CharField(max_length=200, null=True, blank=True)
    order_notes = models.CharField( max_length=200, null=True, blank=True )  

    def __str__(self):
        return self.customer.username


class Review(models.Model):
    product = models.ForeignKey(
        Product , on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    review = models.IntegerField()
    review_text = models.CharField( max_length=200, null=True, blank=True )  
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} review by {self.user.username}'  


class Payment(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    amount = models.FloatField()
    pay_on_delivery = models.BooleanField(default=False , null=True, blank=True)  
    complete = models.BooleanField(default=False , null=True, blank=True)  
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.username


class Delivery(models.Model):
    STATUS = Choices(
        ('doorstep', ('delivery to doorstep')),
        ('pickup', ('delivery to pick up point')),
    )
   # [..]
    option = models.CharField(
       max_length=32,
       choices=STATUS,
       default=STATUS.doorstep,
    )   

class Pickup(models.Model):
    pickup_location = models.CharField(max_length=122)
    active = models.BooleanField(default=False)  

    def __str__(self):
        return self.pickup_location 
        