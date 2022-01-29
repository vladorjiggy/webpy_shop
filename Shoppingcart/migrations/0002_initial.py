# Generated by Django 4.0 on 2022-01-24 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Useradmin', '0001_initial'),
        ('Shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Useradmin.shopuser'),
        ),
        migrations.AddField(
            model_name='payment',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Useradmin.shopuser'),
        ),
    ]