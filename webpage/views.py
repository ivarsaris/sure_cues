from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Repair
from django.core.mail import send_mail

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
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_message = request.POST['message-message']

        # send mail when submitting contact form
        send_mail(
            'Message from ' + message_name,
            message_message,
            message_email,
            ['ivarsaris@gmail.com'],
        )

        return render(request, 'webpage/contact.html', {'message_name': message_name, 'title': 'Contact'})

    else:
        return render(request, 'webpage/contact.html', {'title': 'Contact'})