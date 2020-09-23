from django.urls import path
from .views import (
    SellerSignUpView,
    SellerDashBoardView, 
    SellerProductAddView,
    SellerPdtEditView,
    SellerProductsView,
    SellerOrdersView,
    SellerSettingsView,
    UserDashBoardView,
    UserDashBoardOrdersView
)
urlpatterns = [
    path('seller_reg/', SellerSignUpView.as_view(), name='seller_reg'),
    path('seller/', SellerDashBoardView.as_view(), name='seller_dash'),
    path('seller/add-pdt/', SellerProductAddView.as_view(), name='seller_add_pdt'),
    path('seller/edit-pdt/<int:pk>/', SellerPdtEditView.as_view(), name='seller_edit_pdt'),
    path('seller/pdts/', SellerProductsView.as_view(), name='seller_pdts'),
    path('seller/orders/', SellerOrdersView.as_view(), name='seller_orders'),
    path('seller/<int:pk>/', SellerSettingsView.as_view(), name='seller_settings'),
    path('dashboard/<int:pk>/', UserDashBoardView.as_view(), name='user_dash'),
    path('dashboard/<int:pk>/orders/', UserDashBoardOrdersView.as_view(), name='user_orders'),
]