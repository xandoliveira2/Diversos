#ordenação vetor
import random
lista = [random.randint(1,1000) for i in range(0,49)]
copia = lista.copy()
for i in range(0,len(lista)):
    for j in range(0,len(lista)):
        if lista[i] < lista[j]:
            varlocal = lista[i]
            lista[i]=lista[j]
            lista[j]=varlocal

copia.sort()
print(lista==copia)


lista1 = [2,4,100,200]
lista4 = [[2,4,6],[8,10,12],[200]]
lista5 = [j * 10 for i in lista4 for j in i if len(i)>2]
listai= [1,2,3,4,5,6,7,8,9]
listal = [('impar')if i%2==1 else ('par') for i in listai]
print(listal)
print(lista5)
lista2 = [i * 2 for i in lista1]
print(lista1)
print(lista2)
lista3 = [i * 3 for i in lista1 if i>10]
print(lista3)


def ng():
    perguntas = ["Quanto é raiz quadrada de 64?","Quanto é 10³?","Quanto é 90 + 49?"]
    respostas = ["A)8\nB)16\nC)9\nD)4","A)10\nB)100\nC)1000\nD)10000","A)140\nB)141\nC)139\nD)149"]
    resposta = ["A","C","C"]
    acertos = 0
    for i in range(0,len(perguntas)):
        print("Pergunta número",i+1)
        print(perguntas[i])
        print(respostas[i])
        usuario = input("Enter (A,B,C or D):")
        if usuario.upper() == resposta[i]:
            acertos+=1
 
    porcentagem = float(acertos * 100 / len(perguntas))
    print(f"Você acertou:{acertos}.Uma taxa de :{porcentagem:.2f}%")

class objeto:
    def __init__(self,nome:str,idade:int):
        self.nome = nome
        self.idade = idade
obj = objeto("Alexandre",21)



print(hash(obj))
print(hash('a'))
print(hash('B'))
print(hash('k'))
from time import sleep
sleep(1)
print(hash(obj))
print(hash('a'))
print(hash('B'))
print(hash('k'))