
arvore_geral = [
    [19],
[13,17],
[7,11,3,7],
[5]

]
potencia = 0
ponteiro = 0

def take_left_side():
    retornar = [arvore_geral[0][0]]
    pot = 0
    for i in range(1,len(arvore_geral)):
        retornar.append(arvore_geral[i][0:2**pot])
        pot+=1
    return retornar
def take_right_side():
    retornar = [arvore_geral[0][0]]
    pot = 0
    for i in range(1,len(arvore_geral)):
        retornar.append(arvore_geral[i][2**pot:])
        pot+=1
    return retornar

def formatar(particao):
    retornar = []
    for i in particao:
        if type(i) == list:
            for j in i:
                retornar.append(j)
        else:
            retornar.append(i)
    return retornar
l = take_left_side()
r = take_right_side()
l = formatar(l)
r = formatar(r)
print(r,'  ',list(reversed(r)))
print(l)
if l == sorted(l) and r == sorted(r):
    print(1)
elif l == list(reversed(sorted(l))) and r == list(reversed(sorted(r))): # tudo errado, preciso criar uma função que retorne ela organizada e desorganizada corretamente
    #o que diabos passou na cabeça p botar essa merda?
    print(2)
else:
    print(0)