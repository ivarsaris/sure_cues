from django.contrib import admin
from .models import GalleryImage, Product, Repair

admin.site.register(Product)
admin.site.register(Repair)
admin.site.register(GalleryImage)