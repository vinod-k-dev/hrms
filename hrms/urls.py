"""hrms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2.6/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import base

# Swagger imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="HRMS API",
        default_version="v1",
        description="HRMS Api's documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vinod@buildblog.in"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)


urlpatterns += [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("core.urls")),
    path("", include("employees.urls")),
]

api_urls = [
    path(
        "api/v1/",
        include(
            [
                path("employees/", include("employees.urls", namespace="employees")),
            ]
        ),
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]


urlpatterns += api_urls
