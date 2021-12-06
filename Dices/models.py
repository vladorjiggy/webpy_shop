from django.db import models
# Create your models here.


class Dice(models.Model):
    SIDES = [
        ('D4', '4 Seiten'),
        ('D6', '6 Seiten'),
        ('D8', '8 Seiten'),
        ('D10', '10 Seiten'),
        ('D12', '12 Seiten'),
        ('D20', '20 Seiten'),
    ]

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    colour = models.CharField(max_length=50)
    sides = models.CharField(max_length=3,
                             choices=SIDES)
    prize = models.FloatField(max_length=6)
    image = models.ImageField(upload_to='dice_pictures/', blank=True, null=True)


class Meta:
    ordering = ['sides', 'name']
    verbose_name = 'Dice'
    verbose_name = 'Dice'


def __str__(self):
    return self.name + '(' + self.sides + ')'


def __repr__(self):
    return self.name + '/' + self.description + '/' + self.colour + '/' + self.sides + '/' + self.prize
