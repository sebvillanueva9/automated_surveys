from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cargar/', views.cargar_archivo, name='cargar_archivo'),
    path('descargar/', views.descargar_zip, name='descargar_zip'),
    path('logout/', views.logout_view, name='logout')
]
