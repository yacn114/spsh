# Generated by Django 4.1.7 on 2023-04-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0025_rename_image_preview_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='hot_price',
            field=models.IntegerField(default=0, verbose_name='قیمت بگایی تخفیف'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pricepercent',
            field=models.IntegerField(default=0, verbose_name='درصد تخفیف'),
        ),
    ]
