from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from Shop.models import Dice

class Review(models.Model):
    # TODO: hier img dateien einfügen für Sterne?
    RATING = [
        ('1', 'ein Stern'),
        ('2', 'zwei Sterne'),
        ('3', 'drei Sterne'),
        ('4', 'vier Sterne'),
        ('5', 'fünf Sterne')
    ]

    text = models.CharField(max_length=1000)
    rating = models.CharField(
        max_length=1,
        choices=RATING,
        default='1'
    )
    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    product_reviewed = models.ForeignKey(
        Dice,
        on_delete=models.CASCADE)

