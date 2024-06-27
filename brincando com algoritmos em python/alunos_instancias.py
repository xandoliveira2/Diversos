"""meutexto = str("sopa de macaco")
index = int(len(meutexto))
indexc = int(len(meutexto))-2"""
#input nome de até 20 letras e sendo o primeiro input numero de instancias que vai ser adicionado e no final de cada nome ter uma nota
from os import system
system('cls')
class solucao:
    minhalista = []
    instancias = int()
    def __init__(self,x:int):
        assert 1 <= x <= 100 
        self.x = x
        solucao.instancias = x
        print("instancia criada")
    def adicionar(x):
        index = int(len(x))
        indexc = int(len(x))-2
        if x[indexc:index] == '10':
            print('sopa')
            if 1< len(x)-3 < 21:
                solucao.minhalista.append(x)
            else:
                raise "Erro! Nome com mais de 20 caracteres" 
        else:
            if 1< len(x)-2 < 21:
                solucao.minhalista.append(x)
            else:
                raise "Erro! Nome com mais de 20 caracteres"    
    def comparacaonome(string):
        index = int(len(string))
        indexc = int(len(string))-2
        if string[indexc:index] == '10':
            for i in solucao.minhalista:
                tamanho = int(len(i)-3)
                if 1 < tamanho < 21:
                    return True
                else:
                    return
        else:
            for i in solucao.minhalista:
                tamanho = int(len(i)-2)
                if 1 < tamanho < 21:
                    return True
                else:
                    return  
    def resultado(string:str):
        index = 0
        for i in solucao.minhalista:
            teste = str(i[0:-2])
            if teste.upper() == string.upper():
                 return print(f"\nIntancia {index}\n{teste}\n")
            index += 1
num = int(input("Digite número de instancias: "))
run = solucao(num)
cont = 0
while cont != run.instancias:
    texto = input("digite nome do aluno e sua nota:")
    solucao.adicionar(texto)
    cont += 1
meutexto = input('Digite o texto: ')
solucao.resultado(meutexto)