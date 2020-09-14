from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import transaction
from .models import CustomUser, Seller


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email')


class SellerSignUpForm(UserCreationForm):
    store_name = forms.CharField()
    address = forms.CharField()
    phone = forms.IntegerField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        seller = Seller.objects.create(user=user)
        seller.store_name.add(*self.cleaned_data.get('store name'))
        seller.address.add(*self.cleaned_data.get('address'))
        seller.phone.add(*self.cleaned_data.get('phone'))
        return user    