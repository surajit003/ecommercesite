from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Vendor(models.Model):
    first_name = models.CharField(max_length=120, db_index=True)
    last_name = models.CharField(max_length=120, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    company = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    mobile_number = PhoneNumberField(unique=True)
    instagram = models.URLField(blank=True, null=True)
    products = models.TextField()
    business_type = models.TextField()
    business_objectives = models.TextField()
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
        unique_together = ("first_name", "last_name", "company")

    def __str__(self):
        return "{}-{}".format(self.first_name, self.last_name)
