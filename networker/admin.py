from django.contrib import admin
from .models import NetworkingUserProfile



@admin.register(NetworkingUserProfile)
class NetworkingUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'referrer')
    list_filter = ('level',)
    ordering = ('level',)
