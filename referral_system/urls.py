from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    # path('product/', include('product.urls')),
]
