from django.views.generic import DetailView, ListView
from .models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import UserProfile

# Create your views here.


class CategoryDetailView(DetailView):
    model = Category
    template_name = "catalog/single_category.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        products = Product.objects.filter(categories__slug=self.kwargs.get("slug"))
        context["object_list"] = products
        context["category"] = Category.objects.all()
        return context


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 10
    template_name = "catalog/home.html"
    login_url = "/ecommerce/accounts/login"

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


class ProductListByCompany(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 10
    template_name = "catalog/home.html"
    login_url = "/ecommerce/accounts/login"

    def get_queryset(self):
        object_list = []
        if self.kwargs.get("slug"):
            profile = UserProfile.objects.filter(company__slug=self.kwargs.get("slug"))
            for p in profile:
                product = Product.objects.filter(created_by=p.user)
                object_list.append(product)
        print("obe", object_list)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(ProductListByCompany, self).get_context_data(**kwargs)
        category_list = []
        if self.kwargs.get("slug"):
            profile = UserProfile.objects.filter(company__slug=self.kwargs.get("slug"))
            print("prpfi", profile)
            for p in profile:
                category = Category.objects.filter(created_by=p.user)
                print("p", category)
                category_list.append(category)
        context["category_list"] = category_list
        return context
