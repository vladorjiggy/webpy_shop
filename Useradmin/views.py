from django.contrib.auth import (
    login as auth_login,
)

from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .forms import MySignUpForm
from .models import ShopUser


class MySignUpView(generic.CreateView):
    form_class = MySignUpForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def form_valid(self, form):
        valid = super(MySignUpView, self).form_valid(form)
        auth_login(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())


class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        print(form.get_user())
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