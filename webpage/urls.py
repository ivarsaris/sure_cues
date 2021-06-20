from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sure-home'),
    path('about/', views.about, name='sure-about'),
]