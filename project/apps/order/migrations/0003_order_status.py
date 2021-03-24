# Generated by Django 3.1.5 on 2021-03-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_address_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Open', 'Open - currently active'), ('Process', 'Process - superceded by another basket'), ('Delivered', 'Delivered - for items to be purchased later'), ('Cancel', 'Cancel - the basket cannot be modified'), ('Refunded', 'Refunded')], default='Open', max_length=128, verbose_name='Status'),
        ),
    ]