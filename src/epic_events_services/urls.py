"""epic_events_services URL Configuration

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
from django.urls import path

BASE_URL = 'EpicEvents/CRM_acces/'

urlpatterns = [
    path(BASE_URL, admin.site.urls, name="administration_interface"),
]

admin.site.site_header = "Epic Events Services"
admin.site.index_title = "Epic Events CRM"
admin.site.site_title = "Epic Events CRM"
admin.AdminSite.site_url = None

