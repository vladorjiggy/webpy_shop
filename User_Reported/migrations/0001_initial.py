# Generated by Django 4.0 on 2021-12-13 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_reported',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', related_query_name='review', to='Reviews.review')),
            ],
        ),
    ]
