from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:pk>/', CatDetailView.as_view(), name='cat_detail'),
    path('sub-category/<int:pk>/', SubCatDetailView.as_view(), name='subcat_detail'),
    path('products/', ListingPageView.as_view(), name='pdt_listing'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='pdt_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<int:pk>/', remove_item_from_cart, name='remove-item-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('search/', SearchResultsListView.as_view(), name='search_results')

]