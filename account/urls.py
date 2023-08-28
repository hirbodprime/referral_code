from django.urls import path , include
from .views import (register_user,
        user_login, 
        user_logout,
        register_with_referral,
        profile_view,
        users_profile_view,

        )

urlpatterns = [
    path('api/',include('account.api.urls')),
    path('signup/',register_user,name='register'),
    path('login/',user_login,name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/<str:username>', users_profile_view, name='users_profile'),
    path('signup/<str:referral_code>/', register_with_referral, name='register_with_referral'),


    

]
