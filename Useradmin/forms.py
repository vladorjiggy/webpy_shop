from django.contrib.auth.forms import UserCreationForm
from .models import ShopUser


class MySignUpForm(UserCreationForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture',)
		# password ist wegen UserCreationForm schon mit dabei
