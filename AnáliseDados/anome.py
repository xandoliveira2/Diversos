import pandas as pd
dadosaleatorios = pd.read_csv("MOCK_DATA.csv") # cria um dataframe direto
tentarexcel = pd.DataFrame(dadosaleatorios)
print(tentarexcel.head(7))
# dicionario = {'nome':['alex',''],'idade':[20,30]} #para criar um dataframe com dicionario é encessario que os campos tenham o mesmo tamanho
# d=pd.DataFrame(dicionario) #criando um dataframe de um dicionario
variavel = dadosaleatorios.describe() #vai dar um resumo como minimo,maximo,media,etc.
# print(dadosaleatorios.loc[1]) # busca por 'axis' (indice do canto esquerdo)
# print(dadosaleatorios.loc[dadosaleatorios['country']=="Japan",['first_name','username','salary']]) #com loc [dadosaleatorios[country]=='Japan'] estou definindo que será selecionado apenas
#onde country for igual a 'Japan', e logo apos usando virgula e abrindo uma lista, eu digito o nome das colunas que eu quero que apareça
# print(dadosaleatorios.loc[dadosaleatorios['first_name']=='Nevile'])
# dadosaleatorios['first_name'] = 'none' # não modifica meu arquivo original
# print(dadosaleatorios)
#  df.loc[linha , coluna]
tentarexcel.to_excel("Macaco.xlsx",sheet_name="macaco")
