# Generated by Django 4.2.1 on 2023-05-20 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]