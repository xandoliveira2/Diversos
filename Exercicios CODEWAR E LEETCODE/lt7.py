#inverta o numero inteiro, entao 1004 vira 4001 e 100 vira 1:
def inverter(x:int):
    x = str(x)
    lista = []
    n = str()
    for i in x:
        lista.insert(0,i)
    for i in lista:
        n += i
    print(int(n))
inverter(1004)