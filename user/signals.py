from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        create_profile(instance)


def create_profile(instance):
    UserProfile.objects.create(user=instance)
