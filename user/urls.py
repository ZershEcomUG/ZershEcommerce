from django.urls import path
from .views import (
    SellerSignUpView,
    SellerDashBoardView, 
    SellerProductAddView
)
urlpatterns = [
    path('seller_reg/', SellerSignUpView.as_view(), name='seller_reg'),
    path('seller/', SellerDashBoardView.as_view(), name='seller_dash'),
    path('seller/add-pdt/', SellerProductAddView.as_view(), name='seller_add_pdt')
]