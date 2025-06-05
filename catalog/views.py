from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .models import Product

# Create your views here.
class ProductListPage(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
