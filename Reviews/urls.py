from django.urls import path
from . import views

urlpatterns = [
    path('reviews/<int:pk>/', views.review_list_1, name='reviews_product'),
    path('reviews/<int:pk>/', views.review_list_2, name='reviews_of_user'),
    path('review/add/<int:pk>', views.review_create, name='review_create'),
    path('review/delete/<int:pk>/', views.review_delete, name='review_delete'),
    path('review/<int:pk>', views.review_detail, name='review_detail')
]
