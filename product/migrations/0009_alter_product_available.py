# Generated by Django 4.2.1 on 2023-07-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(verbose_name='موجود است؟'),
        ),
    ]