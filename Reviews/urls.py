from django.urls import path

import Votes
from . import views

urlpatterns = [
    path('show/<int:pk>/', views.review_list_1, name='reviews_product'),
    path('edit/<int:pk>/', views.review_edit, name='review_edit'),
    path('add/<int:pk>/', views.review_create, name='review_create'),
    path('delete/<int:pk>/', views.review_delete, name='review_delete'),
    path('detail/<int:pk>/', views.review_detail, name='review_detail'),
    path('vote/<int:pk>/<str:helpful_or_not>/', views.vote, name='review_vote'),
]
