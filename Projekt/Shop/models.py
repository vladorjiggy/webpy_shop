from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Dice(models.Model):
    SIDES = [
        'D4 ',
        'D6 ',
        'D8 ',
        'D10',
        'D12',
        'D20',
    ]

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    colour = models.CharField(max_length=50)
    sides = models.Charfield(max_length=3,
                             choices=SIDES)
    prize = models.FloatField(max_length=6)
    image = models.ImageField(upload_to='dice_pictures/', blank=True, null=True)
    evaluation = models.ForeignKey()


class Meta:
    ordering = ['sides', 'name']
    verbose_name = 'Dice'
    verbose_name = 'Dice'


def __str__(self):
    return self.name + '(' + self.sides + ')'


def __repr__(self):
    return self.name + '/' + self.description + '/' + self.colour + '/' + self.sides + '/' + self.prize
