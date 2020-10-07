from .models import Category, SubCategory
from pages.models import Ad

def categories_processor(request):
    categories = Category.objects.all()
    ads = Ad.objects.all()
    # then return your variables
    return {'cates': categories, 'ads':ads}