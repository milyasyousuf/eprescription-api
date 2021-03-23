from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    #
    is_active = models.BooleanField(default=True)
    is_visible_frontend = models.BooleanField(default=True)
    description = models.TextField(default='',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="parent_category")

    class Meta:
        app_label = "catalogue"
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)



class Product(models.Model):
    LABEL_CHOICES = (
        ('S', 'Standalone'),
        ('P', 'Parent'),
        ('C', 'Child')
    )

    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    cost_price = models.FloatField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    product_type = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("catalogue:product", kwargs={
    #         'slug': self.slug
    #     })

    # def get_add_to_cart_url(self):
    #     return reverse("catalogue:add-to-cart", kwargs={
    #         'slug': self.slug
    #     })

    # def get_remove_from_cart_url(self):
    #     return reverse("catalogue:remove-from-cart", kwargs={
    #         'slug': self.slug
    #     })
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Product, self).save(*args, **kwargs)

    class Meta:
        app_label = "catalogue"
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

class ProductMedia(models.Model):
    id = models.AutoField(primary_key=True)
    FILE_CHOICE = (("AUDIO", "AUDIO"), ("IMAGE", "IMAGE"))

    question = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name="media")
    type = models.CharField(max_length=8, choices=FILE_CHOICE, null=True, blank=True)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)


    class Meta:
        app_label = "catalogue"
        db_table = "product_media"
        verbose_name = "Product Media"
        verbose_name_plural = "Product Media"

    def __str__(self):
        return self.id