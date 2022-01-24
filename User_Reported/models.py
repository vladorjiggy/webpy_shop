from django.db import models
from Useradmin.models import get_myuser_from_user, ShopUser
from Reviews.models import Review
from django.conf import settings


class User_reported(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='review_reported_by',
                             related_query_name='review_reported_by',
                             )
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='review',
                               related_query_name='review',
                               )
