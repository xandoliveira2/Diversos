#codigo de barra que tem do 1 até 1000000000 eu acho sla e que se a soma dos numeros for par é dumbo e se for impar é da marca 8-bonito
import os
os.system('cls')
codigo = 2341
class solucao:
    lista = []
    soma = int()
    def separador(x:int):
        x = str(x)
        for i in x:
            solucao.lista.append(int(i))
    def codificacao(x:int):
        solucao.separador(x)
        for i in solucao.lista:
            solucao.soma += i
        if solucao.soma % 2 == 1:
            return '8-bonito'
        else:
            return 'dumbinho'
        

print(solucao.codificacao(codigo))
