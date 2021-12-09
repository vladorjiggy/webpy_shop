# Generated by Django 3.2.9 on 2021-12-08 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Useradmin', '0001_initial'),
        ('Dices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', related_query_name='product', to='Dices.dice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ordered_by', related_query_name='product_ordered_by', to='Useradmin.shopuser')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
