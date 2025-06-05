from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListPage.as_view()),
]
