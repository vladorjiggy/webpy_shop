from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.review_list_1, name='review-list'),
    path('show/<int:pk>/', views.review_detail, name='review-detail'),
    path('show/<int:pk>/vote/<str:helpful_or_not>', views.vote, name='review-vote'),
    path('add/', views.review_create, name='review-create'),
    path('delete/<int:pk>', views.review_delete, name='review-delete'),
]