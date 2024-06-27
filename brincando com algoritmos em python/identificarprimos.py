#verificar se o número é primo

def identificarprimos(x:int,tipo='AE'): #AE  AR  B  =  ApenasExibir, ApenasReturn, Both (ambos)
    cont = 1
    if x == 1:
        print('Número 1 não é número primo nem composto')
    elif x == 2:
        if tipo.upper() == 'AR':
            return True
        elif tipo.upper()=='B':
            print(f'É primo o número {x}')
            return True
        else:
            print(f'É primo o número {x}')
    elif x % 2 == 0:
        if tipo.upper() == 'AR':
            return False
        elif tipo.upper()== 'B':
            print(f'não é primo o número {x}')
            return False
        else:
            print(f'não é primo o número {x}')
    else:
        for i in range(1,(x//2)+2,2):
            if (x / i).is_integer() == True:
                cont +=1
        if cont == 2:
            if tipo.upper() == 'AR':
                return True
            elif tipo.upper()=='B':
                print(f'É primo o número {x}')
                return True
            else:
                print(f'É primo o número {x}')
        elif cont > 2:
            if tipo.upper() == 'AR':
                return False
            elif tipo.upper()== 'B':
                print(f'não é primo o número {x}')
                return False
            else:
                print(f'não é primo o número {x}')
        else:
            print('ue, acho que ocorreu algum erro')
            raise 'Erro no código!'
for i in range(0,1111):
    print(identificarprimos(i,'ar'))

#saida onde: True equivale a primo e False a não-primos