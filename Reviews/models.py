from Useradmin.models import get_myuser_from_user, ShopUser
from django.db import models
from django.utils import timezone
from Dices.models import Dice
from Votes.models import Vote
import logging
from django.conf import settings

class Review(models.Model):
    RATING = [
        ('1', 'ein Stern'),
        ('2', 'zwei Sterne'),
        ('3', 'drei Sterne'),
        ('4', 'vier Sterne'),
        ('5', 'fünf Sterne')
    ]
    title = models.CharField(blank=True, max_length=50)
    text = models.CharField(max_length=1000)
    rating = models.CharField(
        max_length=1,
        choices=RATING,
        default='1'
    )
    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )

    product_reviewed = models.ForeignKey(
        Dice,
        on_delete=models.CASCADE,
        )

    def vote(self, user, helpful_or_not):
        myuser = user
        h_or_n = 'H'
        if helpful_or_not == 'not_helpful':
            h_or_n = 'N'
        vote = Vote.objects.create(helpful_or_not=h_or_n,
                                   user=myuser,
                                   review=self)

    def get_helpful_votes(self):
        helpful = Vote.objects.filter(helpful_or_not='H', review=self)
        return helpful

    def get_helpful_count(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.debug('helpful')
        return len(self.get_helpful_votes())

    def get_not_helpful_votes(self):
        not_helpful = Vote.objects.filter(helpful_or_not='N', review=self)
        return not_helpful

    def get_not_helpful_count(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.debug('not helpful')
        return len(self.get_not_helpful_votes())
    
    def get_all_votes(self):
        votes = Vote.objects.filter(review=self)
        return votes








