from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Repair, GalleryImage, CarouselImage, ShaftSpec
from django.core.mail import send_mail

def home(request):
    info = {
        'carousel_images': CarouselImage.objects.all(),
        'title': home
    }
    return render(request, 'webpage/index.html', info)

def impressum(request):
    info = {
        'title': impressum
    }
    return render(request, 'webpage/impressum.html', info)

def products(request):
    info = {
        'products': Product.objects.all(),
        'shaftSpecifications': ShaftSpec.objects.all(),
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
    info = {
        'gallery_images': GalleryImage.objects.all(),
        'title': 'About'
    }
    return render(request, 'webpage/about.html', info)

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