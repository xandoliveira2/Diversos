# discos = int(input())
# ordem = input()
# # 3 estados : 000 inicial 111 final 101 3 lugares diferentes, 100 2 lugares diferentes favoravelmente 001 2 lugares diferentes desfavoravelmente

# #ordem >
# # 1_1
# # 2_3
# # 3_7
# # 4_7+(2*2*2) = 15
# # 5_15+(2*2*2*2) [5_15+16]

# def qtdemaxima(discos):
#     retorno = 0
#     for vezes in range(discos):
#         retorno += 2**vezes
#     return retorno


n = int(input())
seq = input().split(' ')

sum = 0
for i in range(n):
    if seq[i] == '1':
        exp = n - i - 1
        sum += pow(2, exp)

total = pow(2, n) - 1
answer = total - sum

print(answer)