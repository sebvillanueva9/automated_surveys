from django.urls import path
from . import views  # Importa el módulo views
from .views import CargarArchivoAPI  # Importa CargarArchivoAPI desde views.py

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cargar/', views.cargar_archivo, name='cargar_archivo'),
    path('descargar/', views.descargar_zip, name='descargar_zip'),
    path('logout/', views.logout_view, name='logout'),
        # Rutas de la API
    path('api/cargar_archivo/', CargarArchivoAPI.as_view(), name='api_cargar_archivo')
]
