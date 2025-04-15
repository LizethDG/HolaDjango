from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # --- NUEVA RUTA PARA EL REGISTRO ---
    # Llama a la vista 'registro_usuario' cuando se accede a /registro/
    path('registro/', views.registro_usuario, name='registro_usuario'),
    # ---------------------------------
    # Añade más rutas según necesites...
]