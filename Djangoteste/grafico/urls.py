from django.urls import path
from .views import density_map_view,enviar_coluna_data

urlpatterns = [
    path('density-map/', density_map_view, name='density_map_view'),
    path('density-map/requisicao',enviar_coluna_data,name='enviar_coluna_data'),
]