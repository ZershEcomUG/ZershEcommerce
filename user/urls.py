from django.urls import path
from .views import SellerSignUpView, SellerDashBoardView

urlpatterns = [
    path('seller_reg/', SellerSignUpView.as_view(), name='seller_reg'),
    path('seller/<int:pk>/', SellerDashBoardView.as_view(), name='seller_dash')
]