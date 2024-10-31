from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,QueryDict
from django import forms
import django as dj
import plotly.express as pe
from plotly.offline import plot
import pandas as pd
import pymongo as pm
from django.views.decorators.csrf import csrf_exempt
import json
def hours_to_decimals_convertion(formato:str):
    """
    formato : horas:minutos:segundos:direção (latitude e longitude)\n
    exemplo: 29°30'29"W\n
    Converte latitude e longitude no formato decimal para aplicar no gráfico de mapa
    que puxa por valores decimais
    """
    if 'S' in formato or 'W' in formato or 'N' in formato or 'E' in formato:

        if 'S' in formato or 'W' in formato:
            negativo = True
        else:
            negativo = False
        formato = formato.replace('S', '').replace('N', '').replace('W', '').replace('E', '')
        try:
            horas = float(formato.split('°')[0])
        except:
            horas = 0.0
        try:
            minutos = float(formato.split('°')[1].split("'")[0])
        except:
            minutos = 0.0
        try:        
            segundos = float(formato.split("'")[1].removesuffix('"'))
        except:
            segundos = 0.0
        decimal = horas + (minutos / 60) + (segundos / 3600)
        if negativo:
            decimal *= -1
        return decimal
    else:
        return formato
def dcolor(value:int|float) -> str:
    """Gera o a cor o qual aquele valor será representado no mapa, cujo valores são:\n
    vermelho para maior que 50\n
    laranja para maiores que 35 e menor que 51\n
    amarelo para maiores que 25 e menor que 36\n
    azul para maiores que 15 e menor que 26\n
    verde para menores que 16\n
    opacidade 55 representado em hexadecimal equivale a 33% de opacidade"""
    if value > 50:
        return '#ff000055'
    elif value > 35:
        return '#ffa50055'
    elif value > 25:
        return '#ffff0055'
    elif value > 15:
        return '#0000ff55'
    else:
        return '#00ff0055'
client = pm.MongoClient('mongodb://localhost:27017/')
db = client['teste']
collection = db['simlulandodados1']
df = pd.DataFrame(collection.find())
df['latitude_atualizada'] = df['latitude'].apply(hours_to_decimals_convertion)
df['longitude_atualizada'] = df['longitude'].apply(hours_to_decimals_convertion)
df['color'] = df['total'].apply(dcolor)
df['identificador_rua'] = df['latitude_atualizada'].astype(str)+df['longitude_atualizada'].astype(str)
df['data'] = pd.to_datetime(df['data'],format='%d/%m/%Y') 
df['data'] = df['data'].dt.strftime('%d/%m/%Y') 
df['size_column'] = df['total'].apply(lambda x: x if x != 0 else 0.1)
# Importações necessárias

# Classe do formulário



# View principal
# def density_map_view(request):

#     df_filtered1 = df

    


#     df_filtered1['Total de veículos '] = df_filtered1['total'].apply(lambda x: f' {x}')
#     df_filtered1['Quantidade de carros '] = df_filtered1['motos'].apply(lambda x: f' {x}')
#     df_filtered1['Quantidade de motos '] = df_filtered1['carros'].apply(lambda x: f' {x}')
    

#     density_map = pe.scatter_mapbox(
#         df_filtered1,
#         lat='latitude_atualizada',
#         lon='longitude_atualizada',
#         mapbox_style="carto-darkmatter",
#         center={'lat': -22.436491574441884, 'lon': -46.823405867130425},
#         zoom=14,
#         size='size_column',
#         range_color=[10, 60],
#         color_continuous_scale='Viridis',
#         opacity=0.6,
#         custom_data=['total', 'motos', 'carros'],
#         color='color',
#         color_discrete_map={'red': 'red', 'blue': 'blue', 'green': 'green', 'orange': 'orange'},
#     )
#     density_map.update_traces(
#         hovertemplate="<b> Total de veículos</b>: %{customdata[0]}<br>"
#                       "<b>Quantidade de motos</b>: %{customdata[1]}<br>"
#                       "<b>Quantidade de carros</b>: %{customdata[2]}<br><extra></extra>",
#     )
#     density_map.update_layout(showlegend=False)

#     density_map_json = density_map.to_json()
    
#     return render(request, 'density_map.html', {
#         'density_map_json': density_map_json,  # O JSON do mapa que você criou
         
#     }
#                   )


# class DensityFilterForm(forms.Form):

#     df = df.sort_values('data')
#     data_choices = [(data, data) for data in df['data'].unique()]
#     dia = forms.ChoiceField(choices=data_choices)
@csrf_exempt
def recebe_data(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        dado_recebido = dados.get('data')
        
        return JsonResponse({'status':'sucesso','dado_recebido':dado_recebido})
    else:
        return JsonResponse({'erro':'Método não permitido'},status=405)


def enviar_coluna_data(request):
    coluna_dados = df['data'].unique().tolist()
    return JsonResponse({'dados':coluna_dados})

def enviar_coluna_horarios(request):
    data = request.GET.get('param1')
    horas = df[df['data']==data]['horario'].unique().tolist()
    return JsonResponse({'horas':horas})
    
def density_map_view(request):
    filtro = request.GET.get('param1')
    
    df_filtered1 = df[df["data"] == filtro]
    df_filtered1['Total de veículos '] = df_filtered1   ['total'].apply(lambda x : f' {x}')
    df_filtered1['Quantidade de carros '] = df_filtered1['motos'].apply(lambda x : f' {x}')
    df_filtered1['Quantidade de motos '] = df_filtered1['carros'].apply(lambda x : f' {x}')
    df_filtered1['size_column'] = df_filtered1['total'].apply(lambda x: x if x != 0 else 0.1)

    # Cria o gráfico
    density_map = pe.scatter_mapbox(
        df_filtered1,
        lat='latitude_atualizada',
        lon='longitude_atualizada',
        mapbox_style="carto-darkmatter",
        center={'lat': -22.436491574441884, 'lon': -46.823405867130425},
        zoom=14,
        size='size_column',
        range_color=[10, 60],
        color_continuous_scale='Viridis',
        opacity=0.6,
        custom_data=['total', 'motos', 'carros'],
        color='color',
        color_discrete_map={'red': 'red', 'blue': 'blue', 'green': 'green', 'orange': 'orange'},
    )
    density_map.update_traces(
    hovertemplate="<b> Total de veículos</b>: %{customdata[0]}<br><b>Quantidade de motos</b>: %{customdata[1]}<br><b>Quantidade de carros</b>: %{customdata[2]}<br><extra></extra>",
    )
    density_map.update_layout(showlegend=False)
    grafico_html = plot(density_map,output_type='div')
    # density_map_json = density_map.to_json()
    
    return render(request, 'density_map.html',{'grafico_html':grafico_html})

def update_map(request):
    df_filtered1 = df
    df_filtered1['Total de veículos '] = df_filtered1   ['total'].apply(lambda x : f' {x}')
    df_filtered1['Quantidade de carros '] = df_filtered1['motos'].apply(lambda x : f' {x}')
    df_filtered1['Quantidade de motos '] = df_filtered1['carros'].apply(lambda x : f' {x}')
    df_filtered1['size_column'] = df_filtered1['total'].apply(lambda x: x if x != 0 else 0.1)

    # Cria o gráfico
    density_map = pe.scatter_mapbox(
        df_filtered1,
        lat='latitude_atualizada',
        lon='longitude_atualizada',
        mapbox_style="carto-darkmatter",
        center={'lat': -22.436491574441884, 'lon': -46.823405867130425},
        zoom=14,
        size='size_column',
        range_color=[10, 60],
        color_continuous_scale='Viridis',
        opacity=0.6,
        custom_data=['total', 'motos', 'carros'],
        color='color',
        color_discrete_map={'red': 'red', 'blue': 'blue', 'green': 'green', 'orange': 'orange'},
    )
    density_map.update_traces(
    hovertemplate="<b> Total de veículos</b>: %{customdata[0]}<br><b>Quantidade de motos</b>: %{customdata[1]}<br><b>Quantidade de carros</b>: %{customdata[2]}<br><extra></extra>",
    )
    density_map.update_layout(showlegend=False)
    grafico_html = plot(density_map,output_type='div')
    # density_map_json = density_map.to_json()
    
    return render(request, 'density_map.html',{'grafico_html':grafico_html})
# Create your views here