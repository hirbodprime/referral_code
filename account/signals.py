from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile 
from .utils import generate_referral_code , generate_user_unique_code
import random

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not UserProfile.objects.filter(user=instance).exists():
        print('here')
        referral_code = generate_referral_code()  # Generate the referral code
        code = generate_user_unique_code()
        UserProfile.objects.create(user=instance, referral_code=referral_code,user_unique_code=code)


@receiver(post_save, sender=User)
def create_user_unique_code(sender, instance, created, **kwargs):
    if created:  # Make sure the user instance is just created
        try:
            user_profile = UserProfile.objects.get(user=instance)
            if not user_profile.user_unique_code:
                code = generate_user_unique_code()
                user_profile.user_unique_code = code
                user_profile.save()
        except UserProfile.DoesNotExist:
            pass  # Handle the case where UserProfile doesn't exist yet
