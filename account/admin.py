from django.contrib import admin
from .models import UserProfile , CustomUser



admin.site.register(CustomUser)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_unique_code', 'referral_code', 'referrer', 'used_referral_count', 'referral_level')  # Customize displayed fields

admin.site.register(UserProfile, UserProfileAdmin)
