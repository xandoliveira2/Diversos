# knapsack I/O backtracking (1)

nome = ["Livro","Fone","Celular","Carregador"]
peso = [1,2,3,2]
valor = [1,2,5,3]
capacidade = 5


dp = [
    [0 for _ in range(capacidade + 1)] for _ in range(len(peso) + 1)
]


for i in range(1,len(peso)+1):
    for j in range(capacidade + 1):
        if peso[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], valor[i-1]+ dp[i-1][j - peso[i-1]])



# for a in dp:
#     print(a)


cap = capacidade
usou = []

for i in range(len(peso) ,0,-1):
    # print(i)
    if dp[i][cap] != dp[i-1][cap]:
        usou.append(nome[i-1])
        cap -= peso[i-1]

print(f"Valor total carregado = {dp[-1][-1]} e usou os itens {",".join(usou)}")
# print(usou)








