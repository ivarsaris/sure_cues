from django.shortcuts import render
from .models import Product

posts = [
    {
        'author': 'Andreas',
        'title': 'news1',
        'content': 'I have a new website!',
        'date': '20-05-2021'
    }, 
    {
        'author': 'Andreas',
        'title': 'news2',
        'content': 'I have a new home!',
        'date': '20-06-2021'
    }
]

def home(request):
    info = {
        'products': Product.objects.all(),
        'title': 'Home'
    }
    return render(request, 'webpage/index.html', info)

def about(request):
    return render(request, 'webpage/about.html', {'title': 'About'})