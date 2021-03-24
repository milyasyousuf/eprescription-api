
# Create your views here.
from rest_framework import status
from project.apps.order import utils
from project.apps.order.models import Basket, Order, Address, Basket, BasketItem
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import views
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
from project.apps.order.serializer import CheckoutSerializer, BasketSerializer, ShippingAddressSerializer, BasketItemSerializer

from rest_framework.generics import CreateAPIView



class ShippingAddresView(viewsets.ModelViewSet):

    serializer_class = ShippingAddressSerializer
    permission_classes = [
        # IsAuthenticated,
    ]
    queryset = Address.objects.all()
    http_method_names = ["post","get"]

class CheckoutView(CreateAPIView):
    """
    Prepare an order for checkout.

    POST(basket, shipping_address, user):
    {
        "basket": 1,
        "user":1,
        "shipping_address": {
            "country": "Pakistan",
            "city":"Karachi"
            "address": "Roemerlaan 44",
            "notes": "Niet STUK MAKEN OK!!!!",
            "phone_number": "+31 26 370 4887",
            "postcode": "7777KK",
        }
    }
    returns the order object.
    """
    serializer_class = CheckoutSerializer
    permission_classes = [
        # IsAuthenticated,
    ]
    queryset = Order.objects.filter()
    http_method_names = ["post",]
    



class OrderView(viewsets.ModelViewSet):

    serializer_class = CheckoutSerializer
    permission_classes = [
        # IsAuthenticated,
    ]
    queryset = Order.objects.all()
    http_method_names = ["get", "delete"]

class BasketView(viewsets.ModelViewSet):

    serializer_class = BasketSerializer
    permission_classes = [
        # IsAuthenticated,
    ]
    queryset = Basket.objects.all()
    http_method_names = ["get", "delete", "post"]

class BasketItemView(viewsets.ModelViewSet):

    serializer_class = BasketItemSerializer
    permission_classes = [
        # IsAuthenticated,
    ]
    queryset = BasketItem.objects.all()
    http_method_names = ["get", "delete", "post"]