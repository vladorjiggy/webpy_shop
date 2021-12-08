from django.db import models

import Reviews.models
from Useradmin.models import get_myuser_from_user, ShopUser
#from Reviews.models import Review
#from django.db.models import get_model
#MyModel = get_model('app_name', 'ModelName')


class Vote(models.Model):
    VOTE_TYPES = [
        ('H', 'Helpful'),
        ('N', 'Not Helpful')
    ]

    helpful_or_not = models.CharField(max_length=1,
                                      choices=VOTE_TYPES)
    
    user = models.ForeignKey(ShopUser,
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
