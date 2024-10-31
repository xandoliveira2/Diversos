from django.urls import path
from .views import density_map_view,enviar_coluna_data,recebe_data,enviar_coluna_horarios,update_map

urlpatterns = [
    path('density-map/', update_map , name='density_map_view'),
    path('density-map/requisicao/',enviar_coluna_data,name='enviar_coluna_data'),
    path('density-map/receber-dado/',recebe_data, name='recebe_data'),
    path('density-map/requisicao/horarios',enviar_coluna_horarios,name='enviar_coluna_horarios'),
]
