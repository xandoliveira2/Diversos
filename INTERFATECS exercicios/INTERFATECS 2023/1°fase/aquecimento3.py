#o input pode ser varios números, e a saida tem q ser se a soma de todos esses numeros são impar ou par
class solucao:
    def ult_ind(x):
        tipo = type(x)
        x= str(x)
        return tipo(x[len(x)-1])
    def impar_par(lista:list):
        resposta = int()
        for i in lista:
            resposta += solucao.ult_ind(i)
        if solucao.ult_ind(resposta) % 2 == 1:
            return 'impar'
        else:
            return 'par'
listateste = [1,2,3,4,5,6,7,8,9,0,1,4,5,6,7,1231245123412,41241234123123,451352352523456,4574574574564,645745745745,764574574563456276348,1247823187512852,1489725783871]
print(solucao.impar_par(listateste))

def oi(x):
    if x >0:
        raise KeyError
oi(-10)