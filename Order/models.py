from django.db import models
from Useradmin.models import get_myuser_from_user, ShopUser
from Dices.models import Dice


class Order(models.Model):
    user = models.ForeignKey(ShopUser,
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
