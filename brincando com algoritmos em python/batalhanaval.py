#batalha naval? teste1 tentando criar interface de 8 x 8
import random
campos = ('A1','B1','C1','D1','E1','F1','G1','H1',
          'A2','B2','C2','D2','E2','F2','G2','H2',
          'A3','B3','C3','D3','E3','F3','G3','H3',
          'A4','B4','C4','D4','E4','F4','G4','H4',
          'A5','B5','C5','D5','E5','F5','G5','H5',
          'A6','B6','C6','D6','E6','F6','G6','H6',
          'A7','B7','C7','D7','E7','F7','G7','H7',
          'A8','B8','C8','D8','E8','F8','G8','H8',
          )
camposprint = [
          ['A1','B1','C1','D1','E1','F1','G1','H1'],
          ['A2','B2','C2','D2','E2','F2','G2','H2'],
          ['A3','B3','C3','D3','E3','F3','G3','H3'],
          ['A4','B4','C4','D4','E4','F4','G4','H4'],
          ['A5','B5','C5','D5','E5','F5','G5','H5'],
          ['A6','B6','C6','D6','E6','F6','G6','H6'],
          ['A7','B7','C7','D7','E7','F7','G7','H7'],
          ['A8','B8','C8','D8','E8','F8','G8','H8'],
          ]
navios = list(random.choices(campos,k=8))
while True:
    if navios[0] == navios[1] or navios[0] == navios[2] or navios[0] == navios[3] or navios[0] == navios[4] or navios[0] == navios[5] or navios[0] == navios[6] or navios[0] == navios[7] or navios[1] == navios[2] or navios[1] == navios[3] or navios[1] == navios[4] or navios[1] == navios[5] or navios[1] == navios[6] or navios[1] == navios[7] or navios[2] == navios[3] or navios[2] == navios[4] or navios[2] == navios[5] or navios[2] == navios[6] or navios[2] == navios[7] or navios[3] == navios[4] or navios[3] == navios[5] or navios[3] == navios[6] or navios[3] == navios[7] or navios[4] == navios[5] or navios[4] == navios[6] or navios[4] == navios[7] or navios[5] == navios[6] or navios[5] == navios[7] or navios[6] == navios[7]:
        print('Carregando')
        navios = list(random.choices(campos,k=8))
    else:
        break           
for i in camposprint:
    print(i)
embarcacoes = 8
tirol = list()
while embarcacoes != 0:
    tiro = str(input('Digite um campo para atirar: '))
    if tirol.count(tiro.upper()) == 0:
        tirol.append(tiro.upper())
    elif tirol.count(tiro.upper()) == 1:
        print('Já atirou nessa posição, atire denovo.')
        continue
    if tiro.lower() in ',.;':
        print('Você saiu do jogo!')
        break
    if tiro.upper() in navios:
        print(f'Você acertou \n restam ainda {embarcacoes - 1} embarcações')
        embarcacoes -= 1
        for i in camposprint:
            for c in i:
                if c == tiro.upper():
                    camposprint[camposprint.index(i)][i.index(c)] = 'X'              
    else:
        for i in camposprint:
            for c in i:
                if c == tiro.upper():
                   camposprint[camposprint.index(i)][i.index(c)] = 'O'
        print(f'voce errou, tente novamente.\n ainda faltam {embarcacoes} embarcações ')
    for i in camposprint:
        print(i)
if embarcacoes == 0:
    print('Parabéns, você afundou todas embarcações inimigas')
print('FIM DE JOGO')
          

    
    
