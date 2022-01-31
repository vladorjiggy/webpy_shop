# Generated by Django 4.0 on 2022-01-24 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User_Reported', '0001_initial'),
        ('Useradmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_reported',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_reported_by', related_query_name='review_reported_by', to='Useradmin.shopuser'),
        ),
    ]
