from django.urls import path

# from core.views import *
from . import views 

urlpatterns = [
    path('', views.homePage, name="home"),
    
    
]