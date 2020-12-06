from django.urls import reverse
from common.models import TimeStampedModel
from django.db import models


class Category(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Unique value for product page URL, created from name.",
    )
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(
        "Meta Keywords",
        max_length=255,
        help_text="Comma-delimited set of SEO keywords for meta tag",
    )
    meta_description = models.CharField(
        "Meta Description", max_length=255, help_text="Content for description meta tag"
    )

    class Meta:
        db_table = "categories"
        ordering = ["-created_at"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:category_detail", args=[str(self.slug)])


class Product(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text="Unique value for product page URL, created from name.",
    )
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, default=0.00
    )
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(
        max_length=255, help_text="Comma-delimited set of SEO keywords for meta tag"
    )
    meta_description = models.CharField(
        max_length=255, help_text="Content for description meta tag"
    )
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = "products"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:product", args=[str(self.slug)])

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None


class ProductImage(TimeStampedModel):
    category = [
        ("thumbnail", "thumbnail"),
        ("other", "other"),
    ]
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField()
    img_category = models.CharField(max_length=20, choices=category, default="other")

    def __str__(self):
        return "{} {}".format(self.product.name, self.img_category)

    class Meta:
        db_table = "product_images"
        ordering = ["-created_at"]
