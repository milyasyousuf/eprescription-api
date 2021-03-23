
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
#from django_countries.fields import CountryField
from project.apps.catalogue.models import Product
from django.utils.translation import gettext_lazy as _

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    OPEN, MERGED, SAVED, FROZEN, SUBMITTED = (
        "Open", "Merged", "Saved", "Frozen", "Submitted")
    STATUS_CHOICES = (
        (OPEN, _("Open - currently active")),
        (MERGED, _("Merged - superceded by another basket")),
        (SAVED, _("Saved - for items to be purchased later")),
        (FROZEN, _("Frozen - the basket cannot be modified")),
        (SUBMITTED, _("Submitted - has been ordered at the checkout")),
    )
    status = models.CharField(
        _("Status"), max_length=128, default=OPEN, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class BasketItem(models.Model):
    basket = models.ForeignKey('Basket',on_delete=models.CASCADE,related_name='lines',verbose_name=_("Basket"))
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    def is_item_available(self):
        return self.item.is_available

    def validate_stocks(self):
        return self.quantity <= self.item.stock
    
    def validate_basket_status(self):
        return self.basket.status == Basket.OPEN

    def is_exists(self):
        return BasketItem.objects.filter(basket=self.basket, item=self.item).exists()

    def clean(self):
        if not self.validate_basket_status():
            raise ValidationError('Basket status should be open in order to add the item')

        if self.is_exists():
            raise ValidationError('Requested item already exists in the basket, please update the quantity in previosuly added product')

        if not self.is_item_available():
            raise ValidationError('Requested item is out of stock')

        if not self.validate_stocks():
            raise ValidationError('Available stocks is lower then requested stocks, available stocks for the item {}'.format(self.item.stock))

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(BasketItem, self).save(*args, **kwargs)
