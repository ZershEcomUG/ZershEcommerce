from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from .forms import CheckoutForm
from django.contrib import messages
from .models import *

# Create your views here.
class ListingPageView(ListView):
    pass

class SubCatDetailView(DetailView):
    pass

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class CartView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(customer=self.request.user, complete=False)
            context = {
                'object': order,
            }
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")
    



#Function to handle adding items to cart or 
# updating quantity of item incase it's already a cart item     

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk) 
    orderitem, created = OrderItem.objects.get_or_create(
        product=product, customer=request.user, complete=False)
    order_qs = Order.objects.filter(customer=request.user, complete=False)
    if order_qs:
        order = order_qs[0]
        if order.orderitem_set.filter(product = product):
            orderitem.quantity +=1
            orderitem.save()
            messages.info(request , "This product quantity was updated in your cart")
            return redirect('cart') 
        else:
            order.orderitem_set.add(orderitem)    
            messages.info(request , "This product was added to your cart")
            return redirect('pdt_detail', pk =pk ) 
    else:
        order = Order.objects.create(customer=request.user)
        order.orderitem_set.add(orderitem)
        messages.info(request , "This product was added to your cart")
        return redirect('pdt_detail', pk =pk )  


#function to handle removal of item from cart
@login_required
def remove_from_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    order_qs = Order.objects.filter(customer=request.user, complete=False)
    if order_qs:
        order = order_qs[0]
        if order.orderitem_set.filter(product = product):
            orderitem = OrderItem.objects.filter(
            product=product, customer=request.user, complete=False)[0]
            order.orderitem_set.remove(orderitem)
            messages.info(request , "This product was removed from your cart")
            return redirect('cart' )
        else:
            messages.info(request , "This product was not in your cart")
            return redirect('pdt_detail', pk =pk ) 
    else:
        messages.info(request , "You do not have an active order")
        return redirect('pdt_detail', pk =pk )
   

@login_required
def remove_item_from_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    order_qs = Order.objects.filter(customer=request.user, complete=False)
    if order_qs:
        order = order_qs[0]
        if order.orderitem_set.filter(product = product):
            orderitem = OrderItem.objects.filter(
            product=product, customer=request.user, complete=False)[0]
            if orderitem.quantity > 1:
                orderitem.quantity -=1
                orderitem.save()
            else:
                order.orderitem_set.remove(orderitem)
            messages.info(request , "This product quantity was updated ")
            return redirect('cart' )
        else:
            messages.info(request , "This product was not in your cart")
            return redirect('pdt_detail', pk =pk ) 
    else:
        messages.info(request , "You do not have an active order")
        return redirect('pdt_detail', pk =pk )



class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm
        context = {
            'form':form
        }
        return render(self.request, 'checkout.html', context )

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            print('form is valid')
            return redirect('checkout')
