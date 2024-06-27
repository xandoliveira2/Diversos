class Equipes:
    listaglobal = []
    def __init__(self,fatec,equipe,acertos,tempo):
        self.fatec = int(fatec)
        self.equipe =int(equipe)
        self.pontuacao = int(acertos * 100001 - tempo)
    def organizarfatec():
        listaresultado = list('-' * len(Equipes.listaglobal))
        contador = 0
        for i in Equipes.listaglobal:
            contador = 0
            for j in Equipes.listaglobal:
                if i.pontuacao < j.pontuacao:
                    contador +=1 
            while True:
                if listaresultado[contador] == '-':
                    listaresultado[contador] = i
                    break
                else:
                    contador+=1       
        return listaresultado
def main():
    entrada = input().split(' ')
    vagas =int(entrada[0])
    fatecs = int(entrada[1])
    equipes =int(entrada[2])
    for _ in range(equipes):
        a = input().split(' ')
        b = Equipes(int(a[0]),int(a[1]),int(a[2]),int(a[3]))
    listaresultado = []
    b = []
    local = Equipes.organizarfatec()
    remover = []
    for i in range(len(local)):
        if local[i].fatec not in b:
            remover.append(local[i])
            listaresultado.append(local[i].equipe)
            b.append(local[i].fatec)
    for i in remover:
        local.remove(i)
    vagas = vagas - fatecs
    contador = 0
    while vagas != 0:
        listaresultado.append(local[contador].equipe)
        vagas -=1
        contador+=1
    c = sorted(listaresultado)
    print(c)
main()
#bosta de algoritmo demorou mais doque o previsto pq tinha um enorme problema entre o computador e a cadeira e ainda ficou horroroso