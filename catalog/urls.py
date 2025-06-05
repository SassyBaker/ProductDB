from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListPage.as_view(), name='product-list'),
    path('<pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]
