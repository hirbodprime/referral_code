from django.contrib import admin
from .models import SubscriptionLevelModel, UserEarningsModel


@admin.register(SubscriptionLevelModel)
class SubscriptionLevelModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'weekly_earning_limit')

@admin.register(UserEarningsModel)
class UserEarningsModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_level')
