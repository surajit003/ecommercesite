from django.views.generic import DetailView, ListView
from .models import Product, Category

# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = "catalog/item_list.html"


class ProductDetail(DetailView):
    model = Product
    template_name = "catalog/single_product.html"


class CategoryDetail(DetailView):
    model = Category
    template_name = "catalog/single_category.html"
