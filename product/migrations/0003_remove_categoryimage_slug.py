# Generated by Django 4.2.2 on 2023-07-05 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_slug_alter_categoryimage_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryimage',
            name='slug',
        ),
    ]
