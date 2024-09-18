# Version 1
# def move_zeros(lst):
#     contador = 0
#     while True:
#         if 0 not in lst:
#             break
#         contador+=1
#         lst.remove(0)
#     for i in range(contador):
#         lst.append(0)
#     return lst 

#Version 2
def move_zeros(lst):
    contador = lst.count(0)
    while 0 in lst:
        lst.remove(0)
    for i in range(contador):
        lst.append(0)
    return lst
