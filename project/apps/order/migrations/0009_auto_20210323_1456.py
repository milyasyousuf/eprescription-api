# Generated by Django 3.1.5 on 2021-03-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_remove_order_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
