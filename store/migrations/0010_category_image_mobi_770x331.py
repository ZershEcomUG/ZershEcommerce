# Generated by Django 3.1.2 on 2021-03-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_payment_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_mobi_770x331',
            field=models.ImageField(blank=True, null=True, upload_to='cat_imgs/mobi'),
        ),
    ]