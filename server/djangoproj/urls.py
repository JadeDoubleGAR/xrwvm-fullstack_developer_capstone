"""djangoproj URL Configuration.

The `urlpatterns` list routes URLs to views.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path(
        "login/",
        TemplateView.as_view(template_name="index.html"),
    ),
    path("admin/", admin.site.urls),
    path(
        "contact/",
        TemplateView.as_view(template_name="Contact.html"),
    ),
    path(
        "register/",
        TemplateView.as_view(template_name="index.html"),
    ),
    path(
        "about/",
        TemplateView.as_view(template_name="About.html"),
    ),
    path(
        "djangoapp/",
        include("djangoapp.urls"),
    ),
    path(
        "",
        TemplateView.as_view(template_name="Home.html"),
    ),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)
