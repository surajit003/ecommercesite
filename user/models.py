from django.db import models
from django.conf import settings
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=120, unique=True, db_index=True)
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Unique value for company URL, created from name.",
    )
    active = models.BooleanField(default=True)
    image = ResizedImageField(size=[120, 120], quality=75)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        thumbnail = self.image.url
        return thumbnail

    def get_absolute_url(self):
        return reverse("user:company_detail", args=[str(self.slug)])

    class Meta:
        verbose_name_plural = "Companies"


class UserProfile(models.Model):
    role_type = (
        ("VE", "Vendor"),
        ("BU", "Buyer"),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_id = models.UUIDField(max_length=255, default=uuid.uuid4, db_index=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True
    )
    role = models.CharField(max_length=30, choices=role_type, default="VE")
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.user.username
