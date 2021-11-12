# Generated by Django 3.2.9 on 2021-11-10 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_publish_date_books_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='available_status',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='books',
            name='published_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
