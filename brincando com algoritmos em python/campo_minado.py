from random import random,randint
def gerar_matriz(linhas,colunas):
    matriz = [list('' for j in range(colunas)) for i in range(linhas)] 
    return matriz
def colocar_bombas(matriz,quantidade):
    index_coluna = len(matriz[0])-1
    index_linhas = len(matriz)-1
    assert quantidade < index_coluna+1 * index_linhas+1
    bombas_alocadas = 0
    while bombas_alocadas < quantidade:
        if matriz[randint(0,index_linhas)][randint(0,index_coluna)] != 'b':
            matriz[randint(0,index_linhas)][randint(0,index_coluna)] = 'b'
            bombas_alocadas+=1
    return matriz
def colocar_números(matriz): # verificar sobre index de matriz ainda
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 'b':
                pass
            else:
                if i == 0 and j == 0:
                    
