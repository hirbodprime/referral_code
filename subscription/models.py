from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class SubscriptionLevelModel(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    weekly_earning_limit = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    def __str__(self):
        return self.name
    
class UserEarningsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_level = models.ForeignKey(SubscriptionLevelModel, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}, {self.subscription_level}'
    