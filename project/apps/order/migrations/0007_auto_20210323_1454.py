# Generated by Django 3.1.5 on 2021-03-23 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20210323_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
    ]
