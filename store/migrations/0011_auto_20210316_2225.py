# Generated by Django 3.1.2 on 2021-03-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_category_image_mobi_770x331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image_mobi_770x331',
            field=models.ImageField(blank=True, null=True, upload_to='cat_imgs'),
        ),
    ]
