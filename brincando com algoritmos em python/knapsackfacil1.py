# knapsack I/O sem backtrack (2)

peso = [1,2,3,4]
valor = [3,4,5,8]
espaco = 6

dp = [
    [0 for _ in range(espaco + 1)] for _ in range(len(peso) + 1)
]



for i in range(1,len(peso)+1):
    for j in range(espaco + 1):
        if peso[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], valor[i-1] + dp[i-1][j - peso[i-1]])

print(dp[-1][-1])
