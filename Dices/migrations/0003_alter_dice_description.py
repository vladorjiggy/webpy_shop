<<<<<<< Updated upstream
# Generated by Django 4.0.1 on 2022-01-31 09:38
=======
# Generated by Django 4.0.1 on 2022-01-31 09:53
>>>>>>> Stashed changes

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dices', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dice',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
