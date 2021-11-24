from django.db import models
from django.contrib.auth.models import User
from Shop.models import Dice


class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='product_ordered_by',
                             related_query_name='product_ordered_by',
                             )
    product = models.ForeignKey(Dice,
                             on_delete=models.CASCADE,
                             related_name='product',
                             related_query_name='product',
                             )
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'