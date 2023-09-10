# Generated by Django 4.2.4 on 2023-09-09 23:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created datetime'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated datetime'),
        ),
    ]
