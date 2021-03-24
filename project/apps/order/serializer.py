from rest_framework import exceptions, serializers
from project.apps.order.models import Basket, Address, Order, BasketItem


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Address

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Basket

class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BasketItem


class CheckoutSerializer(serializers.ModelSerializer):
    shipping_address = ShippingAddressSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = Order

