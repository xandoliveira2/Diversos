# x = 6  #0110        
# y = 9  #1001 
# #1010 1011 1100 1101 1110 1111

# print(x,y)
# # | e ^ são diferentes, | compara bit por bit com 'or' , ^ usa uma comparação onde: diferentes retorna 1 e iguais retorna 0
# x = x ^ y  # 0110 ^ 1001 -> 1111 -> 15
# print(x,y)

# y = x ^ y # 1111 ^ 1001 -> 0110 -> 6
# print(x,y)

# x = x ^ y # 1111 ^ 0110 ->1001 -> 9

# print(x,y)
















# def acrescentar(a,b):
#     while len(a)<len(b):
#         a = list(a)
#         a.insert(0,'0')
#     a = ''.join(a)
#     return a



# def xor(a,b):
#     a = bin(a)
#     b = bin(b)
#     a = list(a)
#     a.remove('b')
#     a = ''.join(a)
#     b = list(b)
#     b.remove('b')
#     b = ''.join(b)

#     a = acrescentar(a,b)
#     b = acrescentar(b,a)
#     print(a,b)
#     resultado = ''
#     for i in range(len(a)):
#         if a[i] == b[i]:
#             resultado+='0'
#         else:
#             resultado+='1'
#     return resultado
# print(xor(1,2)) # -> 0111
# print(bin(1^2)) # -> 0011
# print(int(xor(1,2),2))


