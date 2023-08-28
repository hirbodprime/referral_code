from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import NetworkingUserProfile



@receiver(pre_save, sender=NetworkingUserProfile)
def update_user_level(sender, instance, **kwargs):
    print(instance.referrer)
    if instance.referrer:
        referrer_user_profile = NetworkingUserProfile.objects.get(user=instance.referrer)  # Access the related NetworkingUserProfile directly
        referrer_level = referrer_user_profile.level
        instance.level = referrer_level + 1
    else:
        instance.level = 1



