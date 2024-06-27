#ordenar do menor para o maior:
from os import system
system('cls')
lista = [4,1,6724,23623,4325,6643,12,214,214,321,5214,51234,12,6,7,812,45,62]
min = lista[2]
nl = list()
for i in lista:
    for x in range(0,len(lista)):
        print(i)
        if i[x] < min:
            if len(nl) > lista.index(i):
                nl.remove(x)
            else:
                nl.insert(lista.index(i),min)
                
print(nl)