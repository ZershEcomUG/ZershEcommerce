from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from store.models import Product

# Create your views here.


class HomePageView(ListView):
    model = Product
    template_name = 'home.html'


class ListingPageView(ListView):
    pass

class DetailPageView(DetailView):
    pass