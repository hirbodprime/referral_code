
from django.db import models
from direct_sellers.models import DirectSellerModel
from django.contrib.auth import get_user_model
from account.models import UserProfile
from wallet.models import WalletModel
User= get_user_model()


class PurchaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Other purchase-related fields

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        user_profile = UserProfile.objects.get(user=self.user)
        referrer = user_profile.referrer
        
        if referrer:
            direct_seller = DirectSellerModel.objects.get(user=referrer)

            wallet = direct_seller.wallet
            earnings = direct_seller.calculate_earnings(self.amount)
            
            wallet.balance += earnings
            wallet.save()


