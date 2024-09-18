#FIRST VERSION
# def create_phone_number(n):
    # return f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}'

#SECOND VERSION
def create_phone_number(n):
    retornar = ''
    for i in range(len(n)):
        if i == 0:
            retornar+='('
        retornar+=str(n[i])
        if i == 2:
            retornar+=') '
        if i == 5:
            retornar+='-'
    return retornar
print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))