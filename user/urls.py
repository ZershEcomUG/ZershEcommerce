from django.urls import path
from .views import (
    SellerSignUpView,
    SellerDashBoardView, 
    SellerProductAddView,
    SellerProductsView,
    UserDashBoardView,
    UserDashBoardOrdersView
)
urlpatterns = [
    path('seller_reg/', SellerSignUpView.as_view(), name='seller_reg'),
    path('seller/', SellerDashBoardView.as_view(), name='seller_dash'),
    path('seller/add-pdt/', SellerProductAddView.as_view(), name='seller_add_pdt'),
    path('seller/pdts/', SellerProductsView.as_view(), name='seller_pdts'),
    path('dashboard/<int:pk>/', UserDashBoardView.as_view(), name='user_dash'),
    path('dashboard/<int:pk>/orders/', UserDashBoardOrdersView.as_view(), name='user_orders'),
]