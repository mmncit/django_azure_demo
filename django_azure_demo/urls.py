# django_azure_demo/urls.py
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('food.urls')),
    path('admin/', admin.site.urls),
]