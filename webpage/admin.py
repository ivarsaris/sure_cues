from django.contrib import admin
from .models import GalleryImage, Product, Repair, CarouselImage, ShaftSpec

admin.site.register(Product)
admin.site.register(Repair)
admin.site.register(GalleryImage)
admin.site.register(CarouselImage)
admin.site.register(ShaftSpec)