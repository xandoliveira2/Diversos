#oque deve fazer:
#1 é sempre uma exeção, ele sempre muda ele mesmo
#o 2 e o 3 sao primos, obviamente nao existem nada antes deles, então so mudam seus futuros...
# o 4 é influenciado pelo 2, então ele abre 
# se o numero de números inteiros q nao seja 1 que ele for divisivel for par ele sera fechado
# se for impar ele sera aberto, o que deve imprimir

def main():
    lista = list()
    while True:
        entrada = input()
        if entrada == '0':
            break
        numero = int(entrada)
        nvl = [1]
        while numero > 2:
            contador = 0
            
            decrescente = numero - 1
            while True:
                if decrescente == 1:
                    break
                if numero % decrescente == 0:
                    contador +=1
                    decrescente-=1
                else:
                    decrescente-=1
            if contador % 2 == 1:
                nvl.append(numero)
                nvl.sort()
            numero-=1
        if len(nvl)>0:
            lista.append(nvl)
    listaresposta = list()

    for i in lista:
        ns = ''
        for j in i:
            ns += str(j)+' '
        listaresposta.append([ns])     
    for i in listaresposta:
        print(''.join(i).strip())
main()