from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
class ListingPageView(ListView):
    pass

class SubCatDetailView(DetailView):
    pass

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'