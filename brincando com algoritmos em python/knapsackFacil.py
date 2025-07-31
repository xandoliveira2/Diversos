# knapsack I/O sem backtrack (1)

pesoItens = [1,2,3]
valorItens = [2,4,5]
capacidade = 4


dp = [
    [0 for x in range(capacidade + 1)] for _ in range(len(pesoItens)+1)
]


for i in range(1,len(pesoItens)+1):
    for j in range(capacidade + 1):
        if pesoItens[i-1] > j:
            dp[i][j] =  dp[i-1][j] 
        else:
            dp[i][j] = max(dp[i-1][j] , valorItens[i-1] + dp[i-1][j - pesoItens[i-1]] )


print(dp[-1][-1])

