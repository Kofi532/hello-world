from django.urls import path
from . import views
from .views import BasePageView




urlpatterns = [
    path("base/", BasePageView.as_view(), name="base"),

#    path("home", views.home, name="home"),
     

#    path("home", views.home, name="home"),
#    path("reg/", views.register, name="register"),
]