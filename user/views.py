from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView,DetailView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import seller_required


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


class UserDashBoardView():
    pass


@method_decorator( seller_required , name='dispatch')
class SellerDashBoardView(ListView):
    model = Seller
    template_name = 'seller_dashboard.html'
