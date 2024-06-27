import os
os.system('cls')
var1 = [20 , 'minuscula']
campo = ''
for i in range(0,(var1[0]+1)):
    campo += '-'

gabaritoM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
gabaritom = 'abcdefghijklmnopqrstuvwxyz'
if var1[1] == 'maiuscula':
    gb1 = gabaritoM
elif var1[1] == 'minuscula':
    gb1 = gabaritom
else:
    print('valor invalido, tenta novamente')
    quit()
for i in range(0,(var1[0]+1)):
    campo = list(campo)

    campo.pop(0)    
    print(''.join(campo))
    try:
        campo += gb1[i]
    except IndexError:
        pass
    