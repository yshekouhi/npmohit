# Generated by Django 4.2.2 on 2023-07-06 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_delete_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid',
            new_name='total_amount',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='zip_code',
        ),
    ]
