# Generated by Django 4.2.2 on 2023-07-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.CharField(default='', max_length=50, verbose_name='خلاصه'),
        ),
        migrations.DeleteModel(
            name='CategoryPost',
        ),
    ]
