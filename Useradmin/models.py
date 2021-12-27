from django.contrib.auth.models import User
from django.db import models


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


class ShopUser(models.Model):
    TYPES = [
        ('SU', 'Superuser'),
        ('CS', 'Customerservice'),
        ('U', 'User')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPES, default='U')
    profile_picture = models.ImageField(upload_to='user_profile_pictures/', blank=True, null=True)

    def is_authorized(self):
        return is_customerservice_or_superuser(self)


def is_customerservice_or_superuser(self):
    if self.type == 'SU' or self.type == 'CS':
        return True
    else:
        return False
