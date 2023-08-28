from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile 
from direct_sellers.models import DirectSellerModel
from wallet.models import WalletModel
from .utils import generate_referral_code , generate_user_unique_code
import random

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not UserProfile.objects.filter(user=instance).exists():
        referral_code = generate_referral_code()  # Generate the referral code
        code = generate_user_unique_code()
        user_profile = UserProfile.objects.create(user=instance, referral_code=referral_code, user_unique_code=code)
        wallet, wallet_created = WalletModel.objects.get_or_create(user=instance)
        
        if instance.DS_NT == 'Direct-Seller':
            user_direct_seller = DirectSellerModel.objects.create(user=instance, wallet=wallet)
            user_direct_seller.ref_code = referral_code
            user_direct_seller.save()
        if instance.DS_NT == 'Networker':
            pass





@receiver(post_save, sender=User)
def replace_spaces_in_username(sender, instance, created, **kwargs):
    if created:
        instance.username = instance.username.replace(' ', '-')  # Replace spaces with hyphens
        instance.save()
