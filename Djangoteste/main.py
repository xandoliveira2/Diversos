
import django as dj
import plotly.express as pe
import pandas as pd
import pymongo as pm

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

# CONFIGURAÇÃO DA PÁGINA

st.set_page_config(
    page_title='Testando gráficos para PI',
    layout='wide',
    )


# CONEXÃO COM MONGODB
client = pm.MongoClient('mongodb://localhost:27017/')
db = client['teste']
collection = db['simlulandodados1']


# CRIAÇÃO DE DATAFRAME COM INFORMAÇÕES DO MONGODB
df = pd.DataFrame(collection.find())


# CONVERSÃO DA COLUNA 'data' PARA FORMATO DE DATETIME PARA UTILIZAR ALGUMAS FUNCIONALIDADES 
df['data'] = pd.to_datetime(df['data'],format='%d/%m/%Y') #-> retorna 2024-10-15 00:00:00 -> passando qual representa dia, mes e ano e logo após formatando no modelo dos EUA, então ele joga o dia p final etc.
df['data'] = df['data'].dt.strftime('%d/%m/%Y') #-> declaro que é para retornar o dia primeiro, depois o mês e depois o ano, sem horário

# ORGANIZANDO O DATAFRAME POR DATA
df = df.sort_values('data')

# CRIANDO A SIDEBAR DE DATA PARA VISUALIZAR AS DATAS ORDENADAS
data = st.sidebar.selectbox("Data",df['data'].unique())

# ORGANIZANDO O DATAFRAME POR HORÁRIO
df = df.sort_values('horario')

# REMOVENDO O "ID_OBJETCT" DO DATAFRAME
df = df.drop('_id',axis=1) 

# CRIANDO COLUNAS NOVAS COM LATITUDE E LONGITUDE ATUALIZADAS EM DECIMAL
df['latitude_atualizada'] = df['latitude'].apply(hours_to_decimals_convertion)
df['longitude_atualizada'] = df['longitude'].apply(hours_to_decimals_convertion)

# CRIANDO A COLUNA 'color' E ANEXANDO UMA STRING DE COR A ELA USANDO A FUNCAO dcolor CRIADA PREVIAMENTE
df['color'] = df['total'].apply(dcolor)

# CÓDIGO IMPROVISADO ATÉ A REALIZAÇÃO DA ATUALIZACAO DO BANCO DE DADOS COM O CAMPO DE 'rua' JÁ PREENCHIDO PORÉM REPRESETARÁ O IDENTIFICADOR DA RUA
df['identificador_rua'] = df['latitude_atualizada'].astype(str)+df['longitude_atualizada'].astype(str)

# CRIAÇÃO DE UM FILTRO COM BASE NO DF, QUE RETORNARÁ APENAS O QUAL CUMPRIR AQUELA CONDIÇÃO, OU SEJA, NESSE CASO RETORNA UM NOVO DATAFRAME ONDE A DATA NO DATAFRAME DF SEJA
# IGUAL AO DECLARADO NA SIDEBAR SELECTBOX DA LINHA ATUALMENTE 83 (POSSIVEL MUDANÇA DE LINHA) FAZENDO ASSIM MOSTRAR APENAS DADOS DAQUELE RESPECTIVO DIA
df_filtered = df[df["data"] == data]

# FILTRANDO PARA QUE ruas_filtradas SEJA UM DATAFRAME 'COPIA' ONDE NO DF ORIGINAL, PEGE ONDE A DATA CORRESPONDE A SELECIONADA E PEGA APENA OS identificador_rua DO DF
# ONDE A DATA SEJA A SELECIONADA
ruas_filtradas = df[df['data'] == data]['identificador_rua']

# CRIAÇÃO DA SIDEBAR PARA SELECIONAR AS RUAS (POR ENQUANTO IMPROVISADO COM A CONCATENAÇÃO DE SUA LATITUDE COM LONGITUDE)
localizacoes = st.sidebar.selectbox(
    "Ruas",
    ruas_filtradas.unique(),
    )

# CRIAÇÃO DE UM DATAFRAME PARA MOSTRAR APENAS DADOS DE ONDE A DATA CORRESPONDE A PREVIAMENTE SELECIONADA E O IDENTIFICADOR DA RUA CORRESPONDA AO SEU PREVIAMENTE SELECIONADO TMB
df_filtered_graficoLinha = df[(df['identificador_rua'] == localizacoes) & (df['data'] == data)]
# df_filtered_graficoLinha = df[(df['rua'] == localizacoes) & (df['data'] == data)]     -> para quando atualizar

#CRIAÇÃO DO GRÁFICO DE LINHA
tent_plot1 = pe.line(
    df_filtered_graficoLinha, # DATAFRAME AO QUAL VAI PEGAR OS DADOS
    'horario', # LINHA X
    ['carros','motos','total'], # LINHA Y
    custom_data=['identificador_rua'],
    markers=True,
    hover_data=None,
    hover_name=None,
)

# MODELAGEM DO TEXTO EXIBIDO AO DEIXAR O MOUSE EM CIMA DO PONTO DO GRÁFICO DE LINHA
for i, column in enumerate(['carros', 'motos', 'total']): # PARA CADA INDEX E COLUNA EM CARROS,MOTOS E TOTAL
    tent_plot1.data[i].hovertemplate = f"<b>{column}</b>: %{{y}}<br><extra></extra>" # VOCÊ VAI PEGAR O DADO CARRO E O TEMPLATE DELE SERA SUA COLUNA E O VALOR SERA 
    # O QUE REPRESENTA NA COLUNA y DE SEU DADO (%{{y}} -> representa valores colocados na linha y)
    # O i REPRESENTA O INDEX, ELE PEGA COM BASE NO CRIADO, ENTÃO REPARE QUE NA LINHA Y DO tent_plot1 A ORDEM É carros motos total RESPECTIVAMENTE, ENTAO ESSE i VAI PEGAR DE INDEX NESSES VALORES
    # O TEMPLATE SERÁ CRIADO EM: NOME DA COLUNA, E O SEU VALOR RESPECTIVO DENTRO DO INDEX, OU SEJA, Y REPRESENTA O VALOR DO INDEX APONTADO NO GRÁFICO

# CRIAÇÃO DE UMA 'DIV FLEX' COM ESPAÇO DIVIDIDO EM 2
col1 = st.columns(2)

# ANEXANDO QUE NA PARTE 1 DESSA DIV, VAI ESTAR O tent_plot1 QUE É UM GRÁFICO DE LINHA, ENTÃO ELE OCUPARA O LADO ESQUERO DA DIV, PARA ALOCAR AO DIREITO MUDAR VALOR PARA col1[1]
with col1[0]:
    st.plotly_chart(tent_plot1)

# SELECT BOX PARA FILTRAR POR HORÁRIOS AO VISUALIZAR O GRÁFICO DE MAPA
option = st.selectbox("Horários:",df_filtered['horario'].unique())

# DATAFRAME QUE MOSRTARÁ APENAS DADOS QUE ESTEJAM NO HORARIO E NA DATA DETERMINADAS PELO USUÁRIO
df_filtered1 = df[(df['horario']==option) & (df['data'] == data)]



# GAMBIARRA PARA MOSTRAR DADOS AO BOTAR O MOUSE EM CIMA DE UMA BOLINHA NO GRÁFICO DE MAPA
df_filtered1['Total de veículos '] = df_filtered['total'].apply(lambda x : f' {x}')
df_filtered1['Quantidade de carros '] = df_filtered['motos'].apply(lambda x : f' {x}')
df_filtered1['Quantidade de motos '] = df_filtered['carros'].apply(lambda x : f' {x}')


# CRIAÇÃO DA TABELA size_column PARA GARANTIR QUE QUANDO NÃO TENHA DADOS, PELO MENOS EXIBA UMA BOLA AO INVÉS DE NÃO EXIBIR (0.1 SE ENCAIXA NO MENOR VALOR DA FUNCAO 
#dcolor, O QUE RETORNA SUA COR VERDE)
df_filtered1['size_column'] = df_filtered1['total'].apply(lambda x: x if x != 0 else 0.1)


# CRIAÇÃO DO MAPA DE INTENSIDADE
density_map = pe.scatter_mapbox(
    df_filtered1, #DATAFRAME UTILIZADO PARA GERAR OS DADOS DO MAPA
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

# ADICIONANDO O TEXTO QUE APARECERA AO COLOCAR O MOUSE POR CIMA DA BOLINHA DO MAPA DE INTENSIDADE
density_map.update_traces(
hovertemplate="<b> Total de veículos</b>: %{customdata[0]}<br><b>Quantidade de motos</b>: %{customdata[1]}<br><b>Quantidade de carros</b>: %{customdata[2]}<br><extra></extra>",
)
# PARA A VERSÃO ATUALIZADA ->density_map.update_traces(hovertemplate="<b> %{customdata[3]}</b><br><br><b> Total de veículos</b>: %{customdata[0]}<br><b>Quantidade de motos</b>: %{customdata[1]}<br><b>Quantidade de carros</b>: %{customdata[2]}<br><extra></extra>",)
 
# ESCONDER A INFORMAÇÃO DE CADA BOLINHA QUE APARECE NO CANTO DIREITO
density_map.update_layout(showlegend=False)

# CRIO UMA 'DIV' QUE OCUPA TODO ESPACO POSSIVEL (POIS É DIVIDIDO POR 1)
col2 = st.columns(1)

# COLOCO MEU MAPA DE DENSIDADE NA COLUNA
with col2[0]:
    st.plotly_chart(density_map)