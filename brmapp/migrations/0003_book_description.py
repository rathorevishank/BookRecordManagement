# Generated by Django 4.2.4 on 2023-08-26 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brmapp', '0002_book_picture_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='Default Description'),
        ),
    ]
