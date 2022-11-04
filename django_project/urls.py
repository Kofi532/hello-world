# django_project/urls.py
from django.contrib import admin
from django.urls import path, include  # new
from django.contrib.auth import views as auth_views

from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("about/", include("pages.urls")),
    path("service/", include("pages.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("your-name/", include("pages.urls")),
    path("blog/", include("pages.urls")),
    path('we/', user_views.home, name='home'),
    path('see/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("base/", include("users.urls")),
]