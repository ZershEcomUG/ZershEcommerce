from django.shortcuts import render, get_object_or_404, redirect
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

def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk) 
    orderitem, created = OrderItem.objects.get_or_create(product=product)
    order_qs = Order.objects.filter(customer=request.user, complete=False)
    if order_qs:
        order = order_qs[0]
        if order.orderitem_set.filter(product = product):
            orderitem.quantity +=1
            orderitem.save()
        else:
            order.orderitem_set.add(orderitem)    
    else:
        order = Order.objects.create(customer=request.user)
        order.orderitem_set.add(orderitem)
    return redirect('pdt_detail', pk =pk )    