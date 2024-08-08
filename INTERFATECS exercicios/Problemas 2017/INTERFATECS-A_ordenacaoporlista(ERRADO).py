MAX_TIME = 100000
dados_equipes = []
classificados = []
entradas = input().split(' ')
vagas       = int(entradas[0])
qtd_fatecs  = int(entradas[1])
qtd_equipes = int(entradas[2])
for i in range(0, qtd_equipes):
  entradas = input().split(' ')
  id_fatec           = int(entradas[0])
  id_equipe          = int(entradas[1])
  problemas_feitos   = int(entradas[2])
  tempo_gasto        = int(entradas[3])
  pontuacao = problemas_feitos * MAX_TIME - tempo_gasto
  equipe = []
  equipe.append(id_fatec)
  equipe.append(id_equipe)
  equipe.append(pontuacao)
  dados_equipes.append(equipe)
dados_equipes.sort()
print(dados_equipes)
cont = 0
for i in range(1, qtd_fatecs+1): # vai percorrer conforme tiver de qtd_fatecs, ou seja, se tiver 1 deve percorrer de 1 a 5 para vermos qual é
    if dados_equipes[cont][0] == i:
        maior_pontuacao = -1
        melhor_equipe = 0
        while dados_equipes[cont][0] == i:
            if dados_equipes[cont][2] > maior_pontuacao:
                maior_pontuacao = dados_equipes[cont][2]
                melhor_equipe = dados_equipes[cont][1]
            if cont == qtd_equipes-1:
                break
            cont += 1
        classificados.append(melhor_equipe)
print(dados_equipes)
for dado in dados_equipes:
    if dado[1] in classificados:
       dados_equipes[dados_equipes.index(dado)][2] = 0 
print(dados_equipes)
vagas -= len(classificados)
for proximos_classificados in range(0,vagas):
    print(proximos_classificados)
    maior_pontuacao = -1
    melhor_equipe = 0
    for dados in dados_equipes:
        if dados[2] > maior_pontuacao:
            maior_pontuacao=dados[2]
            melhor_equipe=dados[1]
            index = dados_equipes.index(dados)
    classificados.append(melhor_equipe)
    dados_equipes.pop(index)
classificados.sort()
print(classificados)