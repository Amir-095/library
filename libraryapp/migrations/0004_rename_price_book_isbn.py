# Generated by Django 5.0 on 2023-12-14 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_rename_genre_book_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='price',
            new_name='isbn',
        ),
    ]