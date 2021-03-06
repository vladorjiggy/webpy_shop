# Generated by Django 3.2.8 on 2022-01-17 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Reviews', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helpful_or_not', models.CharField(choices=[('H', 'Helpful'), ('N', 'Not Helpful')], default='H', max_length=1)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_created_for_review', related_query_name='vote_created_for_review', to='Reviews.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_created_by', related_query_name='vote_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vote',
                'verbose_name_plural': 'Votes',
            },
        ),
    ]
