from ecommerce.celery_app import celery_app as app
from django.utils.text import slugify
from .models import UserProfile, Company


@app.task(name="update_profile")
def update_profile(profile_id, company_name, phone_number, role):
    company = Company.objects.filter(name__iexact=company_name)[0]
    if not company:
        company_slug = slugify(company_name)
        company = Company.objects.create(name=company_name, slug=company_slug)
    UserProfile.objects.filter(profile_id=profile_id).update(
        company=company, phone_number=phone_number, role=role
    )
