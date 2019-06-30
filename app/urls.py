from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.regstrar_estacionaiento, name='registro_estacionamiento'),
    path('mapa/', views.mapa, name='mapa'),
]