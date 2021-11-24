from django.db import models
from django.contrib.auth.models import User
from Reviews.models import Review


class Votes(models.Model):

    status = models.BooleanField()
    
    user = models.ForeignKey(User,
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