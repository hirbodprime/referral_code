from django.urls import path
from .views import  dashboard_view
from django.views.generic.base import RedirectView

urlpatterns = [

    path('', RedirectView.as_view(url='dashboard/', permanent=True)),
    path('dashboard/', dashboard_view, name='dashboard'),

]
