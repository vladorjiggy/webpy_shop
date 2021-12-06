from django.contrib.auth import (
    login as auth_login,
)
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .forms import MySignUpForm
from .models import ShopUser
from Useradmin.models import get_myuser_from_user


class MySignUpView(generic.CreateView):
    form_class = MySignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password'],
                                        first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        email=data['email'],
                                        )
        my_user = ShopUser.objects.create(user=user,
                                          profile_picture=data['profile_picture']
                                          )
        print(user)
        print(my_user)
        return redirect('login')


class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        """Security check complete. Log the user in. PERFORM CUSTOM CODE."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())


class MyUserListView(generic.ListView):
    model = ShopUser
    context_object_name = 'all_myusers'
    template_name = 'myuser-list.html'

class SingleUserView(generic.DetailView):
    model = ShopUser
    context_object_name = 'single_user'
    template_name = 'single_user.html'