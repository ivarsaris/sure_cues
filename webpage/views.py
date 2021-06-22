from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Repair

def home(request):
    return render(request, 'webpage/index.html', {'title': 'Home'})

def products(request):
    info = {
        'products': Product.objects.all(),
        'title': 'Products'
    }
    return render(request, 'webpage/products.html', info)

def repairs(request):
    info = {
        'repairs': Repair.objects.all(),
        'title': 'Repairs'
    }
    return render(request, 'webpage/repairs.html', info)

def about(request):
    return render(request, 'webpage/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'webpage/contact.html', {'title': 'Contact'})