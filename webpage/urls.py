from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sure-home'),
    path('products/', views.products, name='sure-products'),
    path('about/', views.about, name='sure-about'),
    path('repairs/', views.repairs, name='sure-repairs'),
    path('contact/', views.contact, name='sure-contact'),
]