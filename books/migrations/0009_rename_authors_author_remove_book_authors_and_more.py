# Generated by Django 4.0.1 on 2022-01-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_remove_authors_book_book_authors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='books.Author'),
        ),
    ]