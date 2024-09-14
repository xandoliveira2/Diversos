
arvore_geral = [
    [1],
[2,3],
[4,5,6,7]

]
potencia = 0
ponteiro = 0

def take_left_side():
    retornar = [arvore_geral[0][0]]
    pot = 0
    for i in range(1,len(arvore_geral)):
        retornar.append(arvore_geral[i][0:2**pot])
        pot+=1

    print(retornar)


take_left_side()