# Generated by Django 3.2.8 on 2022-01-17 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dice',
            old_name='user',
            new_name='superuser',
        ),
    ]