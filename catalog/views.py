from django.views.generic import DetailView, ListView
from .models import Product, Category

# Create your views here.


class ProductList(ListView):
    model = Product
    paginate_by = 10
    template_name = "catalog/home.html"


class ProductDetail(DetailView):
    model = Product
    template_name = "catalog/product.html"


class CategoryList(ListView):
    model = Category
    template_name = "catalog/category.html"


class CategoryDetail(DetailView):
    model = Category
    template_name = "catalog/category.html"
