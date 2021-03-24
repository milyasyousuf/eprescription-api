from django.contrib import admin
from project.apps.order.models import Basket,BasketItem, Order, Address


# Register your models here.
admin.site.register(BasketItem)
admin.site.register(Basket)
admin.site.register(Order)
admin.site.register(Address)