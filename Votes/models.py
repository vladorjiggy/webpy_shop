from django.db import models
from Useradmin.models import get_myuser_from_user, ShopUser
from Reviews.models import Review


class Votes(models.Model):

    status = models.BooleanField()
    
    user = models.ForeignKey(ShopUser,
                             on_delete=models.CASCADE,
                             related_name='vote_created_by',
                             related_query_name='vote_created_by',
                             )
    review = models.ForeignKey(Review,
                             on_delete=models.CASCADE,
                             related_name='vote_created_for_review',
                             related_query_name='vote_created_for_review',
                             )
    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'