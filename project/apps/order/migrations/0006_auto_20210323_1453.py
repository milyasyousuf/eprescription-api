# Generated by Django 3.1.5 on 2021-03-23 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_basket_basket_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='received',
        ),
        migrations.RemoveField(
            model_name='order',
            name='refund_granted',
        ),
        migrations.RemoveField(
            model_name='order',
            name='refund_requested',
        ),
    ]
