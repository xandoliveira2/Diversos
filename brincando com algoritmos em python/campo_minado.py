from random import random,randint
def gerar_matriz(linhas,colunas,preenchimento:str=''):
    """
    Gera matriz com linhas e colunas informados 
    """
    matriz = [list(preenchimento for j in range(colunas)) for i in range(linhas)] 
    return matriz
def colocar_bombas(matriz,quantidade):
    """
    Preenche a matriz com bombas aleatorias com base na quantidade de bombas informadas no segundo parametro
    """
    
    index_coluna = len(matriz[0])-1
    index_linhas = len(matriz)-1
    LIMITE_BOMBAS_MAXIMO = len(matriz) * len(matriz[0])
   
    assert 1 <= quantidade < LIMITE_BOMBAS_MAXIMO
    bombas_alocadas = 0
    while bombas_alocadas < quantidade:
        if matriz[randint(0,index_linhas)][randint(0,index_coluna)] != 'b':
            matriz[randint(0,index_linhas)][randint(0,index_coluna)] = 'b'
            bombas_alocadas+=1
    return matriz
def mapear(matriz:list):
    """ 
    Retorna um dicionário com os vizinhos de todas as posições da matriz informada (ou seja, 0,0 tem como vizinho 0,1 1,0 e 1,1 por exemplo)
    """
    mapeado = dict()
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            mapeado[(linha,coluna)] = []
            for movimentacao_x in [-1,0,1]:
                if linha + movimentacao_x < 0 or linha+movimentacao_x>=len(matriz):
                    continue
                for movimentacao_y in [-1,0,1]:
                    if coluna+movimentacao_y < 0 or coluna+movimentacao_y>=len(matriz[0]):
                        continue
                    if linha + movimentacao_x == linha and coluna+movimentacao_y == coluna:
                        pass
                    else:
                        mapeado[(linha,coluna)].append((linha + movimentacao_x,coluna+movimentacao_y))
    return mapeado

def verificar_bombas(vizinhos:list,matriz_base):
    """
    Coloca números de bombas ao seu arredor (metodo suplementar da função 'colocar_números(matriz)'
    """
    bombas = 0
    for posicoes in vizinhos:
        if matriz_base[posicoes[0]][posicoes[1]] == 'b':
            bombas+=1
    return bombas


def colocar_numeros(matriz): 
    """Colocar o valor de cada posição da matriz em um dicionario (exemplo: (0,0) : 3 -> a posicao 0 está cercada de bombas"""
    dicionario_mapeado = mapear(matriz)
    posicoes = dicionario_mapeado.keys()
    lista_bombas = dict()
    for keys in posicoes:
        if matriz[keys[0]][keys[1]] == 'b':
            lista_bombas[keys] = 'b'
        else:
            lista_bombas[keys] = verificar_bombas(dicionario_mapeado[keys],matriz)
    return lista_bombas

def main():
    comeco_matriz = list(map(int,input('Digite dimensoes da matriz linhas e colunas respectivamente separadas por espaço (recomendado que use mesmo valores):').split(' ')))
    matriz_base = gerar_matriz(comeco_matriz[0],comeco_matriz[1])
    while True:
        try:
            matriz_bombas = colocar_bombas(matriz_base,int(bombas :=input(f'Digite quantidade de bombas que deseja no campo (Min = 1 , Máx = {len(matriz_base[0])*len(matriz_base)-1})')))
            break
        except:
            print('\nNúmero excede o limite máximo ou minimo, digite um valor válido\n')
    dicionario_completo = colocar_numeros(matriz_bombas)
    matriz_imprimivel = gerar_matriz(len(matriz_base),len(matriz_base[0]),'#')
    comparacao = matriz_imprimivel[0][0]
    contagem = 0
    for linha in matriz_imprimivel:
        contagem+=linha.count(comparacao)
    verificador = []
    print('\n')
    for linha in matriz_imprimivel:
        print(linha)
    print('\n')
    while True:
        try:
            if contagem == int(bombas):
                print('Parabéns, você evitou todas as bombas')
                break
            entrada_usuario = input('Digite posição para abrir (separados por espaco representando respectivamente linha e coluna)').split(' ')

            if ''.join(entrada_usuario) in verificador:
                print('Você já digitou essa posição, tente outra')
                continue
            verificador.append(''.join(entrada_usuario))

            matriz_imprimivel[int(entrada_usuario[0])-1][int(entrada_usuario[1])-1] = dicionario_completo[(int(entrada_usuario[0])-1,int(entrada_usuario[1])-1)]
            contagem-=1
            for linha in matriz_imprimivel:
                print(linha)

            if matriz_imprimivel[int(entrada_usuario[0])-1][int(entrada_usuario[1])-1] == 'b':
                print('\nVocê acertou em uma mina, que pena, tente novamente')
                break
        except IndexError:
            print('\nNúmeros incorretos, tente novamente\n')
        except KeyError:
            print('\nNúmeros incorretos, tente novamente\n')
        except ValueError:
            print('\nÉ aceito apenas números, evite letras ou quaisquer outros tipos de caracteres\n')
main()