# Generated by Django 3.0.8 on 2020-07-14 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
