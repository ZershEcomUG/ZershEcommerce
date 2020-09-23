from django import forms
from user.models import CustomUser, Seller
from .models import Product
from django.forms import ModelForm


class CheckoutForm(forms.Form):
    phone = forms.IntegerField()
    location = forms.CharField()
    address = forms.CharField()
    building_apartment_name = forms.CharField(required=False)
    order_notes = forms.CharField( required=False , widget=forms.Textarea)

class ReviewForm(forms.Form):
    review = forms.IntegerField()
    review_text = forms.CharField( required=False , widget=forms.Textarea)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'price', 'image_182x182', 'image_1200x1200', 'image_600x600',
            'image_600x600_2', 'image_300x300', 'sku', 'available',  'description', 'brand','category', 'seller'
            ]
