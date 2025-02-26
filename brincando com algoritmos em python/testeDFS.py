import sys
sys.setrecursionlimit(1000)
matriz = [
    [0, 1, 15, 6, 0],
    [1, 0, 5, 14, 3],
    [15, 5, 0, 0, 4],
    [6, 14, 0, 0, 12],
    [0, 3, 4, 12, 0],
]
chaves = {
    '1': {'2','3','4'},
    '2': {'1', '3', '4','5'},
    '3': {'1','2','5'},
    '4': {'1','2','5'},
    '5': {'2','3','4'}
}
permutacoes = []


def retirarIndex(comparacao):
    for i in range(len(permutacoes)):
        if permutacoes[i] == comparacao:
            return i


def dfs(lista: list, limite=5):
    copia = lista.copy()
    proximosDfs = []
    for i in chaves[lista[-1]]:
        copia2 = lista.copy()
        if i not in copia2:
            copia2.append(i)
        if copia2 not in permutacoes:
            proximosDfs.append(copia2)
    listaVdd = []
    for proximos in proximosDfs:
        if len(proximos) > len(lista):
            listaVdd.append(proximos)
            if len(proximos) == limite:
                permutacoes.append(proximos)
    for i in listaVdd:
        dfs(i)


possibilidades = [
    ['1'],
    ['2'],
    ['3'],
    ['4'],
    ['5'],
    ]
for p in possibilidades:
    dfs(p)


for per in permutacoes:
    print(per)
    if per == ['4','1','2','5','3']:
        print("essa provavelmente foi a resposta, porém agora seria ponderado com gráfico de peso")
