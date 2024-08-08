def procurar(matriz):

    for linhas in range(0,len(matriz)):
        
        if ''.join(matriz[linhas][:]) == 'X'*len(matriz[0]):
            return True
        string = ''
        for coluna in range(0,len(matriz)):
            string+=matriz[coluna][linhas]
        if string == 'X'*len(matriz):
            return True
    return False
        


def main():


    dadostotais = []
    entrada = input().split(' ')
    x = int(entrada[0])
    y = int(entrada[1])
    jogadores = int(input())

    for i in range(0,jogadores):
        jogador = []
        for j in range(0,y):
            entrada = input().split()
            jogador.append(entrada)
        dadostotais.append(jogador)
    num_entradas = int(input())
    resultado = []
    for rodada in range(0,num_entradas):
        dado = input()
        for cartela in dadostotais:
            
            # if procurar(dadostotais[dadostotais.index(cartela)]) == True:
                    
            #     local = [str(dadostotais.index(cartela)+1),str(rodada)]
            #     resultado.append(local)
            for linha in cartela:
                for coluna in linha:
                    if coluna == dado:
                        dadostotais[dadostotais.index(cartela)][cartela.index(linha)][linha.index(coluna)] = 'X'
            if procurar(dadostotais[dadostotais.index(cartela)]) == True:
                    
                local = [str(dadostotais.index(cartela)+1),str(rodada+1)]
                resultado.append(local)
            

    



    
    if len(resultado) > 1:
        if resultado[0][1] == resultado[1][1]:
            resultado = 'EMPATE'
        else:
            resultado = f'{resultado[0][0]} {resultado[0][1]}'
    elif len(resultado) < 1:
        resultado = 'NADA'
    else:
        resultado = f'{resultado[0][0]} {resultado[0][1]}'
        
    print(resultado)
main()


