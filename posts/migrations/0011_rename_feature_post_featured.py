# Generated by Django 4.2.2 on 2023-07-14 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_feature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='feature',
            new_name='featured',
        ),
    ]
