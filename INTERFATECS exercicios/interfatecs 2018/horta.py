def main():
    lista = []
    for i in range(0,3):
        casoteste = input().split(' ')
        for i in casoteste:
            lista.append(int(i))
    soma = 0
    for i in range(0,6,2):
        numero = lista[i]//lista[i+1]
        soma+= numero
        
    print(soma,"\n")
main()