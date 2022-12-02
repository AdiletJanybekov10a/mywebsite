from django.urls import path
from . import views

urlpatterns = [
    path('', views.nova_home, name='nova_home'),
    
]
