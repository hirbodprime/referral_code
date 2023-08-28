from django.db import models
from django.contrib.auth import get_user_model
from wallet.models import WalletModel

User = get_user_model()

class DirectSellerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    earnings_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.10)  # 10% earnings
    wallet = models.OneToOneField(WalletModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Direct Seller: {self.user}'
    
    def calculate_earnings(self, purchase_amount):
        earnings = purchase_amount * self.earnings_percentage
        return earnings

