# Generated by Django 4.2 on 2023-06-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesab', '0005_alter_user_prod_tickets'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='subject',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
