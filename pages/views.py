from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from store.models import Category, SubCategory, Product
from pages.models import Slider, PromotionImg
# Create your views here.


class HomePageView(ListView):
    model = SubCategory
    template_name = 'home.html'
    queryset = SubCategory.objects.all()
    pdt = Product.objects.all()
    cat = Category.objects.all()
    promoImg = PromotionImg.objects.all()
    sliderImgs = Slider.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['products'] = self.pdt.order_by('?')[:6]
        context['categories'] = self.cat.order_by('?')[:5]
        context['subcategories'] = self.queryset
        context['sliders'] = self.sliderImgs[:3]
        context['promopics'] = self.promoImg[:3]
        return context
    

