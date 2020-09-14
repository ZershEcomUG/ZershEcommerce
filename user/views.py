from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import SellerSignUpForm
from .models import CustomUser

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
        login(self.request, user)
        return redirect('students:quiz_list')