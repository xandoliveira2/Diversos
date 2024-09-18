"""
operador de identidade = is e is not
representam se está NO MESMO ENDEREÇO 
então:
"""
a = 10
b = 10
c = 10
d = 9
print(id(a))
print(id(b))
print(id(c))
print(id(d))
"""qual a grande sacada, quando você referencia uma variavel com '10' por exemplo, imagino que seja coisa do python, e declara outra variavel com o valor '10', ele não
cria outra variavel com esse valor, ele coloca como valor dessa segunda variavel, o endereco de memoria que já existe o '10', puxando assim diretamente ele, sem usar 
um novo espaço na memória e não se aplica em listas, porque a cada lista ele declara um espaço novo, ele não consegue adentrar dentro da lista e comparar os elementos 
dela (e nem de nenhuma coleção)
OBS: isso se aplica apenas em alguns casos,nem toda string e nem todos inteiros terão esse comportamento, por exemplo inteiro em alguns casos pode quebrar a partir do
numero 257 por conta de espaço de memoria reservado"""
#IF TERNÁRIO
from random import randint
a = randint(0,99)
status = 'par' if a%2==0 else 'impar'
print(f'{a} é um número {status}')