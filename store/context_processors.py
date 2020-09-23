from .models import Category, SubCategory

def categories_processor(request):
    categories = Category.objects.all()
    # then return your variables
    return {'categories': categories}