from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product, Category

# Create your views here.


class ProductDetail(DetailView):
    model = Product
    template_name = "catalog/single_product.html"


class CategoryDetail(DetailView):
    model = Category
    template_name = "catalog/single_category.html"
