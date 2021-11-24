from django.db import models
from django.contrib.auth.models import User
from Reviews.models import Review


class User_reported(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='review_reported_by',
                             related_query_name='review_reported_by',
                             )
    review = models.ForeignKey(Review,
                             on_delete=models.CASCADE,
                             related_name='review',
                             related_query_name='review',
                             )