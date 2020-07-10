from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from store.models import SubCategory, Product
# Create your views here.


class HomePageView(ListView):
    model = SubCategory
    template_name = 'home.html'
    queryset = SubCategory.objects.all()
    pdt = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['products'] = self.pdt.order_by('?')[:6]
        context['subcategories'] = self.queryset
        return context
    

class ListingPageView(ListView):
    pass

class DetailPageView(DetailView):
    pass