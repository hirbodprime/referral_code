from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class NetworkingUserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    referrer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')
    level = models.PositiveIntegerField(null=True, blank=True, default=1)
    
    def __str__(self):
        return f'Networking User Profile - Level: {self.level}'
    
