# Generated by Django 4.1.7 on 2023-03-26 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0023_alter_teachers_options_alter_product_hot_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price_percent',
            new_name='pricepercent',
        ),
    ]
