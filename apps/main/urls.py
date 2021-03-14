from django.urls import path
from .views import index, contact_view

urlpatterns = [
    path("", index, name="home"),
    path("contact", contact_view, name="contact"),
]
