from django.contrib import admin

# Register your models here.
from project.apps.catalogue.models import Product, ProductMedia, Category



# Register your models here.
admin.site.register(Product)
admin.site.register(ProductMedia)
admin.site.register(Category)