# Generated by Django 4.2.2 on 2023-07-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_categoryservice_options_categoryservice_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryservice',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='ترتیب'),
        ),
    ]