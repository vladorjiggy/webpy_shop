from datetime import date, datetime
from django.contrib.auth.models import User
from django.db import models
from Shoppingcart.models import ShoppingCart

from django.contrib.auth.models import AbstractBaseUser


def get_myuser_from_user(user):
    '''
    :param user: Instance from User class
    :return: Corresponding MyUser instance, or None if the
    instance does not exist
    '''
    myuser = None
    myuser_query_set = ShopUser.objects.filter(user=user)
    if len(myuser_query_set) > 0:
        myuser = myuser_query_set.first()
    return myuser


class ShopUser(AbstractBaseUser):
    REQUIRED_FIELDS = ('user',)
    USERNAME_FIELD = 'user'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='user_profile_pictures/', blank=True, null=True)

    def count_shopping_cart_items(self):
        count = 0
        if self.is_authenticated:
            shopping_carts = ShoppingCart.objects.filter(myuser=self)
            if shopping_carts:
                shopping_cart = shopping_carts.first()
                count = shopping_cart.get_number_of_items()

        return count