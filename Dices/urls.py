from django.urls import path, include
from . import views

urlpatterns = [
    path('show/', views.product_list, name='product-list'),
    path('show/<int:pk>/', views.single_product, name='product-detail'),
    path('add/', views.ProductCreateView.as_view(), name='product-create'),
    path('edit/<int:pk>', views.product_edit, name='product-edit'),
    path('reviews/', include('Reviews.urls')),
    path('search/', views.product_search, name='product-search'),
]
