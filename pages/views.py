from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, DetailView
from store.models import Category, SubCategory, Product
from pages.models import Slider, PromotionImg
from .forms import ContactForm
from .models import Contact
# Create your views here.


class HomePageView(ListView):
    model = SubCategory
    template_name = 'home.html'
    queryset = SubCategory.objects.all()
    cat = Category.objects.all()
    promoImg = PromotionImg.objects.all()
    sliderImgs = Slider.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.order_by('?')[:6]
        context['pdts'] = Product.objects.order_by('?')[:12]
        context['categories'] = self.cat
        context['cates'] = self.cat.order_by('?')
        context['subcategories'] = self.queryset
        context['sliders'] = self.sliderImgs[:3]
        context['promopics'] = self.promoImg[:3]
        return context
    

class AboutPageView(TemplateView):
    template_name = 'about-us.html'

    cat = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['cates'] = self.cat.order_by('?')
        return context

class ContactPageView(View):
    def get(self, *args, **kwargs):
        form = ContactForm
        cates = Category.objects.all()
        context = {
            'form':form,    
            'cates':cates,        
        }
        return render(self.request, 'contact.html', context )

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            contact = Contact(
                name = name,
                email = email, 
                subject = subject,
                message = message
            )
            contact.save() 
            return redirect('home')

class PrivacyPageView(TemplateView):
    template_name = 'privacy-policy.html'

    cat = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PrivacyPageView, self).get_context_data(**kwargs)
        context['cates'] = self.cat.order_by('?')
        return context

class TermsPageView(TemplateView):
    template_name = 'terms-and-conditions.html'

    cat = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TermsPageView, self).get_context_data(**kwargs)
        context['cates'] = self.cat.order_by('?')
        return context

class PolicyPageView(TemplateView):
    template_name = 'return-and-order-policy.html'

    cat = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PolicyPageView, self).get_context_data(**kwargs)
        context['cates'] = self.cat.order_by('?')
        return context

class HowToSellPageView(TemplateView):
    template_name = 'become-a-vendor.html'

    cat = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HowToSellPageView, self).get_context_data(**kwargs)
        context['cates'] = self.cat.order_by('?')
        return context

    