from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('repairs/', views.repairs, name='repairs'),
    path('contact/', views.contact, name='contact'),
]