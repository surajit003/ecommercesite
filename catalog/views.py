from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import UserProfile
from .forms import ProductAdminForm
from django.contrib import messages


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
    template_name = "catalog/product/list_products.html"
    login_url = "/ecommerce/accounts/login"

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = "catalog/product/view_product.html"


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


def Index(request):
    return render(request, "catalog/new_core/index.html")


class CreatProduct(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductAdminForm
    template_name = "catalog/product/add_product.html"
    success_message = "Product was created successfully"
    error_message = "Error saving the Doc, check fields below."

    def get_success_url(self):
        return reverse("catalog:product_create")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.slug = form.cleaned_data["name"].lower().replace(" ", "-")
        obj.save()
        return super(CreatProduct, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class ProductUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    # specify the model you want to use
    model = Product
    form_class = ProductAdminForm
    template_name = "catalog/product/update_product.html"
    success_message = "Product was updated successfully"
    error_message = "Error saving the Doc, check fields below."

    def get_success_url(self):
        return reverse("catalog:product_create")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.slug = form.cleaned_data["name"].lower().replace(" ", "-")
        obj.save()
        return super(ProductUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class ProductDelete(DeleteView):
    # specify the model you want to use
    model = Product
    template_name = "catalog/product/delete_product.html"

    def get_success_url(self):
        return reverse("catalog:product_list")
