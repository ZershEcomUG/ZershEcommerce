from django.urls import path
from .views import *

urlpatterns = [
    path('product/<int:pk>/', ProductDetailView.as_view(), name='pdt_detail'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove-from-cart')
]