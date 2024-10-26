#exemplo básico

def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * fatorial(numero-1)
print(fatorial(6))


matriz1 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
retornar = []
#tentando pegar todos os de cima da matriz
def pegar_acima(posicoes1:tuple):
   
    if posicoes1[0] != 0:
 
        retornar.append(posicoes1)
    
        return pegar_acima((posicoes1[0]-1,posicoes1[1]))
    else:

        retornar.append(posicoes1)

        return
    
pegar_acima((2,2))
print(retornar)

# tentando percorrer até o final da matriz com recursividade indo do comeco até o final e depois abaixando
# com base na matriz: matriz1
caminho=[]
def caminhar(posicao_inicial):
    if posicao_inicial == (2,3):
        caminho.append(matriz1[posicao_inicial[0]][posicao_inicial[1]])
        return
    else:
    
        caminho.append(matriz1[posicao_inicial[0]][posicao_inicial[1]])
        if posicao_inicial[1] < 3:
            return caminhar((posicao_inicial[0],posicao_inicial[1]+1))
        else:
            return caminhar((posicao_inicial[0]+1,posicao_inicial[1]))
        
caminhar((0,0))
print(caminho)


#tentando mapear 'ilhas'
ilha1=[
    list('1110'),
    list('1100'),
    list('1000'),
]
ilha2=[
    list('111000011'),
    list('111100011'),
    list('001000001'),
    list('001100000'),
    list('000000111'),
]
quantidade = 0
def definir_possibilidades(matriz):
    x=[i for i in range(len(matriz))]
    y=[i for i in range(len(matriz[0]))]
    combinations = []
    
    for i in x:
        for j in y:
            combinations.append((i,j))
    return combinations

def quantidade_ilhas(matriz):
    combinations = definir_possibilidades(matriz)
    quantidade = 0
    verificados = []
    def verificar_ilhas(cordenadas):
        x= cordenadas[0]
        y=cordenadas[1]
        if matriz[x][y] == 0:
            return
        else:
            print(x,y)
            verificados.append((x,y))
            verificar_ilhas((x+1,y)),verificar_ilhas((x-1,y)),verificar_ilhas((x,y-1)),verificar_ilhas((x,y+1))
    verificar_ilhas((0,0))
    print(verificados)
    
quantidade_ilhas(ilha1)