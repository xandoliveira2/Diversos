# knapsack I/O backtracking (1)

nome = ["Livro","Lancheira","Fone","Power Bank"]
peso = [1,2,3,4]
valor = [2,4,5,7]
capacidade = 6


dp = [
    [0 for _ in range(capacidade + 1)] for _ in range(len(nome)+1)
]


for i in range(1,len(nome)+1):
    for j in range(capacidade + 1):
        if peso[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], valor[i-1] + dp[i-1][j-peso[i-1]])

# for a in dp:
#     print(a)

cap = capacidade
usou = []
for i in range(len(peso) ,0,-1):
    # print(i,cap)
    if dp[i][cap] != dp[i-1][cap]:
        usou.append(nome[i-1])
        cap -= peso[i-1]

print("Max : ",dp[-1][-1])
print("Itens : ", end='')
print(*usou,sep=',')
