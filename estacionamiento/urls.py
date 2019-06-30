from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]