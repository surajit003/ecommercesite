from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.conf import settings


# Create your models here.


class Vendor(models.Model):
    status = (
        ("open", "open"),
        ("taken", "taken"),
        ("closed", "closed"),
    )
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
    admin_checked = models.BooleanField(default=False)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT
    )
    current_status = models.CharField(max_length=30, choices=status, default="open")

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
        unique_together = ("first_name", "last_name", "company")

    def __init__(self, *args, **kwargs):
        print("vendorrr")
        super(Vendor, self).__init__(*args, **kwargs)
        self.__original_status = self.active

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = "{}-{}".format(
                self.first_name.lower().replace(" ", "-"),
                self.last_name.lower().replace(" ", "-"),
            )
        return super(Vendor, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("event:event_detail", args=[str(self.slug)])


class VendorConfirmationCode(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    confirmation_code = models.CharField(max_length=220, db_index=True, unique=True)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.vendor, self.confirmation_code)
