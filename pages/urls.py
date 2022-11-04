# pages/urls.py
from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, ServicePageView


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"), 
    path("", HomePageView.as_view(), name="home"),
    path("service/", ServicePageView.as_view(), name="service"),
]


    
