# django_project/urls.py
from django.contrib import admin
from django.urls import path, include  # new
from django.contrib.auth import views as auth_views
from posts.views import CreatePostView
from users import views as user_views
from pages import views as user_view
from django.conf import settings
from django.conf.urls.static import static
from pages.views import HomePageView, HoPageView, uploadImg
from posts.views import HomePageView, CreatePostView
from posts import views
from posts.views import ExperienceList


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("about/", include("pages.urls")),
    path("service/", include("pages.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
#    path("your-name/", HoPageView.as_view(), name="your-name"),
    path("blog/", include("pages.urls")),
    path('we/', user_views.home, name='home'),
    path('see/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("base/", include("users.urls")),
    path("posthome/", include("posts.urls")),
    path("post/", include("posts.urls")),
    path("dad/", HomePageView.as_view(), name="home"),
    path("mum/", CreatePostView.as_view(), name="post"),
    path("your-name/", user_view.uploadImg, name="display"),
    path('modelview/', views.ExperienceList.as_view(), name='experience_list'),
    
]


if settings.DEBUG:  # new
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
