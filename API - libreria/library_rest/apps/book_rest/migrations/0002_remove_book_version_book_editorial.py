# Generated by Django 4.0.1 on 2022-01-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_rest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='version',
        ),
        migrations.AddField(
            model_name='book',
            name='editorial',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
