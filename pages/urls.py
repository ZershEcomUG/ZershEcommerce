from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about-us/', AboutPageView.as_view(), name='about'),
    path('contact-us/', ContactPageView.as_view(), name='contact'),
    path('privacy-policy/', PrivacyPageView.as_view(), name='privacy'),
    path('terms-conditions/', TermsPageView.as_view(), name='terms'),
    path('order-policy/', PolicyPageView.as_view(), name='order_policy'),
    path('how-to-sell/', HowToSellPageView.as_view(), name='how_to_sell'),
]
