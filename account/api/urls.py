from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView,UserProfileList, UserProfileDetail,UserReferralCodeView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='api-register'),
    path('login/', UserLoginView.as_view(), name='api-login'),
    path('logout/', UserLogoutView.as_view(), name='api-logout'),
    path('profile/', UserProfileList.as_view(), name='user-profile-list'),
    path('profile/<int:pk>/', UserProfileDetail.as_view(), name='user-profile-detail'),
    path('profile/referral-code/', UserReferralCodeView.as_view(), name='user-referral-code'),

    # ... other API URLs ...
]
