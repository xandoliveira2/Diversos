import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as pe
import pymongo as pm
from geopy.geocoders import Nominatim
def decimal_to_degree(formato):
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
geolocator = Nominatim(user_agent="geoapiExercises")

# def pegar_rua(string):
#     lat = string.split(' ')[0]
#     lon = string.split(' ')[1]
#     try:
#         location = geolocator.reverse((lat, lon), )
#        # Adiciona um intervalo de 1 segundo entre as requisições
#         if location is not None:
#             return location.address.split(',')[0]
#         else:
#             return 'Rua não encontrada'
#     except Exception as e:
#         print(f"Erro ao tentar encontrar a rua para as coordenadas ({lat}, {lon}): {e}")
#         return 'Erro'
def dcolor(value):
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

#     if value > 50:
#         return [1.0, 0, 0, 0.2]
#     elif value< 20:
#         return [0, 1.0, 0, 0.2]
#     else:
#         return [0, 0, 1.0, 0.2]

st.set_page_config(page_title='Testando gráficos para PI' , layout='wide')
client = pm.MongoClient('mongodb://localhost:27017/')
db = client['teste']
collection = db['simlulandodados1']
# collection.insert_one(
#     {'carro': 20,
#      'moto': 30,
#      'media': 25,
#      'horario': '13:00',
#      'data': '10/01/2024',
     
#      }
# )
df = pd.DataFrame(collection.find())
df['data'] = pd.to_datetime(df['data'],format='%d/%m/%Y')
df['data'] = df['data'].dt.strftime('%d/%m/%Y')
try:
    df = df.sort_values('data')
    # df = df.sort_values('horario')
    
except:
    pass

data = st.sidebar.selectbox("Data",df['data'].unique())
try:
    df = df.sort_values('horario')
except:
    pass
# horario = st.select_slider("Horario",df['horario'].unique())
# horarios = st.sidebar.selectbox('Horarios',df['horario'].unique())
df = df.drop('_id',axis=1)
df['latitude_atualizada'] = df['latitude'].apply(decimal_to_degree)
df['longitude_atualizada'] = df['longitude'].apply(decimal_to_degree)
# df['rua'] = df.apply(lambda x: pegar_rua(f"{x['latitude_atualizada']} {x['longitude_atualizada']}"), axis=1)

df['color'] = df['total'].apply(dcolor)
# df['Total'] = df['carros']+df['motos']  
# df.reset_index(drop=False,inplace=True)
df['identificador_rua'] = df['latitude_atualizada'].astype(str)+df['longitude_atualizada'].astype(str)

df_filtered = df[df["data"] == data]
# chartline1 = st.line_chart(df_filtered,x='horario',y=['carros','motos','Total'])


# col1 = st.plotly_chart(tent_plot)
col1 = st.columns(2)
col3 = st.columns(1)
df_filtered
ruas_filtradas = df[df['data'] == data]['identificador_rua']

localizacoes = st.sidebar.selectbox("Ruas",ruas_filtradas.unique())
df_filtered_graficoLinha = df[(df['identificador_rua'] == localizacoes) & (df['data'] == data)]
# df_filtered_graficolinha = df[df['rua']]  -> para quando atualizar
df_filtered_graficoLinha
tent_plot1 = pe.line(df_filtered_graficoLinha,
    'horario',
    ['carros','motos','total'],
    custom_data=['identificador_rua'],
    markers=True,
    hover_data=None,
    hover_name=None,
)
for i, column in enumerate(['carros', 'motos', 'total']):
    tent_plot1.data[i].hovertemplate = f"<b>{column}</b>: %{{y}}<br><extra></extra>"
with col1[0]:
    st.plotly_chart(tent_plot1)


option = st.selectbox("Horários:",df_filtered['horario'].unique())
df_filtered1 = df[(df['horario']==option) & (df['data'] == data)]
# df_filtered




df_filtered1['Total de veículos '] = df_filtered['total'].apply(lambda x : f' {x}')
df_filtered1['Quantidade de carros '] = df_filtered['motos'].apply(lambda x : f' {x}')
df_filtered1['Quantidade de motos '] = df_filtered['carros'].apply(lambda x : f' {x}')
# df_filtered1['Horário '] = df_filtered['horario'].apply(lambda x : f' {x}')
# df_filtered1['Data '] = df_filtered1['data'].apply(lambda x : f' {x}')

df_filtered1['size_column'] = df_filtered1['total'].apply(lambda x: x if x != 0 else 0.1)

# st.dataframe(df_filtered1)

""" 
linhas abaixo: criação do mapa de densitidade
"""
density_map = pe.scatter_mapbox(
    df_filtered1,
    lat='latitude_atualizada',
    lon='longitude_atualizada',
    mapbox_style="carto-darkmatter",
    center={'lat': -22.436491574441884, 'lon': -46.823405867130425},
    zoom=14,
    size='size_column' ,
    range_color=[10 , 60],  
    color_continuous_scale='color',#["rgba(0, 0, 255, 1.0)","rgba(0, 255, 0, 1.0)","rgba(255, 0, 0, 1.0)"],#["green", "red"],
    opacity=0.6,
    custom_data=['total','motos','carros'],
    # PARA A VERSÃO ATUALIZADA -> custom_data=['total','motos','carros','rua'],
    #hover_data={'latitude_atualizada':False,'longitude_atualizada':False,'total':False,'color':False,'Total de veículos ':True,'Quantidade de carros ':True,'Quantidade de motos ':True},#'Horário ':True,'Data ':True
    color='color',
    color_discrete_map={"#ff000055":'red','#ffa50055':'orange','#ffff0055':'yellow','#0000ff55':'blue','#00ff0055':'green'},
    color_continuous_midpoint=40,)
density_map.update_traces(hovertemplate="<b> Total de veículos</b>: %{customdata[0]}<br><b>Quantidade de motos</b>: %{customdata[1]}<br><b>Quantidade de carros</b>: %{customdata[2]}<br><extra></extra>",
)
 # PARA A VERSÃO ATUALIZADA ->density_map.update_traces(hovertemplate="<b> %{customdata[3]}</b><br><br><b> Total de veículos</b>: %{customdata[0]}<br><b>Quantidade de motos</b>: %{customdata[1]}<br><b>Quantidade de carros</b>: %{customdata[2]}<br><extra></extra>",)
 
density_map.update_layout(showlegend=False)
with col3[0]:
    st.plotly_chart(density_map)




st.map(df_filtered1,latitude='latitude_atualizada',longitude='longitude_atualizada',size='total',color='color')


# st.write("Valores de 'total':", df_filtered['total'].unique())
# st.write("Valor máximo de 'total':", df_filtered['total'].max())

