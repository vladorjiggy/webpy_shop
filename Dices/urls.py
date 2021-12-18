from django.urls import path, include
from . import views

urlpatterns = [
    path('show/', views.ProductListView.as_view(), name='product-list'),
    path('show/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add/', views.ProductCreateView.as_view(), name='product-create'),
    path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='product-confirm_delete'),
    path('r/', include('Reviews.urls')),
    path('search/', views.book_search, name='product-search'),
]
