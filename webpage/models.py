import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    type = models.IntegerField(default=1)
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='product_images')

    def __str__(self):
        return f'{self.name} Product'

class ShaftSpec(models.Model):
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=40)
    diameter = models.CharField(max_length=40)
    ferrule = models.CharField(max_length=40)
    length = models.CharField(max_length=40)
    joint = models.CharField(max_length=40)
    taper = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name} ShaftSpec'

class Repair(models.Model):
    type = models.IntegerField(default=1)
    name = models.CharField(max_length=40)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return f'{self.name} Repair'

class GalleryImage(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(default='default.jpg', upload_to='gallery_images')

    def __str__(self):
        return f'{self.name} GalleryImage'

class CarouselImage(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(default='default.jpg', upload_to='carousel_images')

    def __str__(self):
        return f'{self.name} CarouselImage'
