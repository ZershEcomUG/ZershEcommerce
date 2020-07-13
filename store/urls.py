from django.urls import path
from .views import *

urlpatterns = [
    path('product/<int:pk>/', ProductDetailView.as_view(), name='pdt_detail'), 
]