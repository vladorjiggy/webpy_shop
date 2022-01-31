from django.db import models
from Useradmin.models import ShopUser
from django.conf import settings

class Vote(models.Model):
    VOTE_TYPES = [
        ('H', 'Helpful'),
        ('N', 'Not Helpful')
    ]

    helpful_or_not = models.CharField(max_length=1,
                                      choices=VOTE_TYPES,
                                      default='H')

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='vote_created_by',
                             related_query_name='vote_created_by',
                             )

    review = models.ForeignKey('Reviews.Review',
                               on_delete=models.CASCADE,
                               related_name='vote_created_for_review',
                               related_query_name='vote_created_for_review',
                               )

    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'
