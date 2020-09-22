from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView,DetailView, UpdateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import seller_required
from store.models import *
from store.forms import ProductForm
from django.contrib import messages


from .forms import SellerSignUpForm
from .models import CustomUser, Seller

# Create your views here.

class SellerSignUpView(CreateView):
    model = CustomUser
    form_class = SellerSignUpForm
    template_name = 'registration/seller_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('seller_dash')


class UserDashBoardView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['username', 'email', 'phone']
    template_name = 'user_dashboard.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your Information was succesfully updated")
        return redirect('user_dash', pk=self.request.user.pk)



class UserDashBoardOrdersView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'user_dash_orders.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(UserDashBoardOrdersView, self).get_context_data( **kwargs)
        context['orders'] = Order.objects.filter(customer=self.request.user)
        #order = Order.objects.get(customer=self.request.user)
        #context['orderitems'] = order.orderitem_set.all()
        return context

@method_decorator( seller_required , name='dispatch')
class SellerDashBoardView(ListView):
    model = Seller
    template_name = 'seller_dashboard.html'

    def get_context_data(self, *args, **kwargs):
        user = CustomUser.objects.get(username=self.request.user.username)
        user1 = user.seller_set.get(store_name=user.username)
        context = super(SellerDashBoardView, self).get_context_data( **kwargs)
        context['products'] = Product.objects.filter(seller=user1).order_by('-id')[:11]
        context['orders'] = OrderItem.objects.all().order_by('-id')
        return context

@method_decorator( seller_required , name='dispatch')
class SellerProductAddView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'seller_add_pdt.html'

    def form_valid(self, form):
        product = form.save()
        messages.success(self.request, "Your Product was succesfully added")
        return redirect('seller_dash')


@method_decorator( seller_required , name='dispatch')
class SellerProductsView(ListView):
    model = Product
    template_name = 'seller_pdts.html'

    def get_context_data(self, *args, **kwargs):
        user = CustomUser.objects.get(username=self.request.user.username)
        user1 = user.seller_set.get(store_name=user.username)
        context = super(SellerProductsView, self).get_context_data( **kwargs)
        context['products'] = Product.objects.filter(seller=user1).order_by('-id')
        return context