from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=120, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    company = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    company_website = models.CharField(max_length=30, blank=True, null=True)
    mobile_number = PhoneNumberField(unique=True)
    instagram = models.URLField(blank=True, null=True)
    products = models.TextField()
    business_type = models.TextField()
    business_objectives = models.TextField()
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
        unique_together = ("name", "company")

    def __str__(self):
        return self.name
