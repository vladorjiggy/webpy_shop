from django.urls import path
from Reviews import views

urlpatterns = [
    path('review-editdelete/<int:pk>/', views.review_edit_delete, name='review_edit_delete'),
    #path('product-editdelete/<int:pk>/', views.product_edit_delete, name='product_edit_delete'),
]