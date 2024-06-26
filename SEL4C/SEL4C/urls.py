"""SEL4C URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.documentation import include_docs_urls
from api  import views
from general import views
from SEL4C_Dashboard import views

urlpatterns = [
    path("", include("general.urls")),
    path("dashboard/", include("SEL4C_Dashboard.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("docs", include_docs_urls(title="Api Documentation")),
    path('<path:not_found>', views.error_404, name='error_404'),
]
