# Generated by Django 3.2.8 on 2022-01-29 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dices', '0002_rename_user_dice_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dice',
            name='superuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_created_by', related_query_name='product_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
