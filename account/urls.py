from django.urls import path , include
from .views import (register_user,
        user_login, 
        view_referral_code, 
        dashboard, 
        user_logout,
        register_with_referral,

        )

urlpatterns = [
    path('api/',include('account.api.urls')),
    path('signup/',register_user,name='register'),
    path('login/',user_login,name='login'),
    path('logout/', user_logout, name='logout'),
    path('view_referral_code/', view_referral_code, name='view_referral_code'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signup/<str:referral_code>/', register_with_referral, name='register_with_referral'),


    

]
