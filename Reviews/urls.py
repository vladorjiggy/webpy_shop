from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:pk>/', views.review_list_1, name='reviews_product'),
    path('list/<int:pk>/', views.review_list_2, name='reviews_of_user'),
    path('add/<int:pk>', views.review_create, name='review_create'),
    path('delete/<int:pk>/', views.review_delete, name='review_delete'),
    path('detail/<int:pk>', views.review_detail, name='review_detail')
]
