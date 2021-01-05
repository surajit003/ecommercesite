from django.views.generic import DetailView, ListView
from .models import Product, Category

# Create your views here.


class ProductList(ListView):
    model = Product
    paginate_by = 10
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = "catalog/product.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context


class CategoryList(ListView):
    model = Category
    template_name = "catalog/category.html"


class CategoryDetail(DetailView):
    model = Category
    template_name = "catalog/category.html"
