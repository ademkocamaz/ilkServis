"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path, include, re_path
from baton.models import BatonTheme

urlpatterns = [
    path("", lambda request: redirect("admin/", permanent=True)),
    path("admin/", admin.site.urls),
    path("baton/", include("baton.urls")),
    re_path(r'^_nested_admin/', include('nested_admin.urls')),
]


admin.site.unregister(BatonTheme)
admin.site.site_url = None
