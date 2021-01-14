from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Unique value for company URL, created from name.",
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    role_type = (
        ("VE", "Vendor"),
        ("BU", "Buyer"),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True
    )
    role = models.CharField(max_length=30, choices=role_type, default="VE")

    def __str__(self):
        return self.user.username
