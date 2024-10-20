from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargar_archivo, name='cargar_archivo'),
    path('descargar/', views.descargar_zip, name='descargar_zip'),
]
