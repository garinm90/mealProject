from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.main.urls")),
    path("accounts/", include("allauth.urls")),
    path("menu/", include("apps.menu.urls", namespace="menu")),
]
