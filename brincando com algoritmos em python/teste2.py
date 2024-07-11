def procurar(matriz):

    for linhas in range(0,len(matriz)):
        print(''.join(matriz[linhas][:]))
        print('X'*len(matriz[0]))
        if ''.join(matriz[linhas][:]) == 'X'*len(matriz[0]):
            return True
        string = ''
        for coluna in range(0,len(matriz)):
            string+=matriz[coluna][linhas]
        if string == 'X'*len(matriz):
            return True
    return False

matriz = [['1','2','X'],
          ['4','5','6'],
          ['X','X','X']]
print(procurar(matriz))