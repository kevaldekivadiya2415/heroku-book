# Generated by Django 4.0.1 on 2022-01-31 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_review_book_id_review_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('book', models.ManyToManyField(to='books.Book')),
            ],
        ),
    ]
