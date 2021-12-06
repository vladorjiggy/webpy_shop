from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('signup/', views.MySignUpView.as_view(), name='signup'),
    path('userprofiles/', views.MyUserListView.as_view(), name='myuser-list'),
    path('userprofiles/<int:pk>/', views.SingleUserView.as_view(), name='single_user'),
]