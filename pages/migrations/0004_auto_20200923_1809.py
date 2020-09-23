# Generated by Django 2.2.16 on 2020-09-23 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_brand'),
        ('pages', '0003_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='associated_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Category'),
        ),
        migrations.AddField(
            model_name='slider',
            name='associated_subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.SubCategory'),
        ),
        migrations.AddField(
            model_name='slider',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='description2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='heading',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='point_to_category',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='point_to_subcateory',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]