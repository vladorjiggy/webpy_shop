# Generated by Django 4.0 on 2021-12-27 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
    ]
