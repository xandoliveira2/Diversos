def fazer_hash(senha:str):
    soma = 0
    for index in range(0,len(senha)):
        soma += ord(senha[index]) * (index+1)
    divisor = divisor_primos(soma)
    return str(soma)+divisor
    
def comparador(lista: list[int]):
    soma = 0
    for item in lista:
        soma*=item
def divisor_primos(numero:int)->str:
    divisores = []
    contador = 2
    while True:
        if comparador(divisores) == numero:
            break
        if (numero/contador).is_integer() and is_primo(contador):
            divisores.append(contador)
            numero = numero / contador
            contador-=1
        contador +=1
        
            
    retornar = str()
    for item in divisores:
        retornar+=str(item)
    return retornar
def is_primo(numero:int)->bool:
    if numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        condicao = 1
        for numeros in range(3,numero//2):
            if (numero/numeros).is_integer():
                condicao+=1
        if condicao > 1:
            return False
        else:
            return True


def main():
    entrada = ''
    while True:
        entrada = input().split(' ')
        if 'ACABOU' in entrada:
            break
        print(entrada[0],fazer_hash(entrada[1]))
main()