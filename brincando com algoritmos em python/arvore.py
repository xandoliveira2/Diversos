def take_left_side(arvore:list)->list[int]:
    """pega parte esquerda da árvore

    Args:
        arvore(list) -> this is the formated tree list

    Returns:
        uma lista com todos numeros da parte esquerda da árvore
    """
    retornar = [arvore[0][0]]
    pot = 0
    for i in range(1,len(arvore)):
        retornar.append(arvore[i][0:2**pot])
        pot+=1
    return retornar
def take_right_side(arvore):
    """right part from tree

    Args:
        arvore(list) -> this is the formated tree list
        

    Returns:
        list[int]: the right int values 
    """
    retornar = [arvore[0][0]]
    pot = 0
    for i in range(1,len(arvore)):
        retornar.append(arvore[i][2**pot:])
        pot+=1
    return retornar

def formatar(particao:list): 
    """remove 'list' inside from another 'list'

    Args:
        particao (list): this should be a list with list inside

    Returns:
        list: list without another lists inside 
    """
    retornar = []
    for i in particao:
        if type(i) == list:
            for j in i:
                retornar.append(j)
        else:
            retornar.append(i)
    return retornar
# def separar_lista(lista:list):
#     pot = 0
#     retornar = [lista[0]]
#     lista.pop(0)
#     while True:
#         try: #                               0  1 2   3 4 5 6   7 8 9  10 11 12 13 14
#             retornar.append(lista[2**pot]) # 1  2,3   4,5,6,7   8,9,10,11,12,13,14,15
#             retornar.append(lista[2**(pot+1)])
#             pot+=1
#         except IndexError:

def separar(lista):
    potencia = 0
    retornar = [lista[0]]
    numero = len(lista)**1/2
    if numero == int(numero):
        numero +=1
    
    for i in range(int(numero)):
        retornar.append(lista[2**potencia:2**potencia+1])
        potencia+=1
    return retornar


def criar_arvore():
    
    vezes = int(input())
    dados_bruto = []
    for i in range(vezes):
        dados_bruto.append(int(input()))
    print(separar(dados_bruto))
criar_arvore()


   
