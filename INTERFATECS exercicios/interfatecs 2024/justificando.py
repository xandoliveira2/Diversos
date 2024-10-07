# inicio 10:16 - fim  10:53
espacamento = int(input())
texto = input().split(' ')
soma = 0
espacos = 0
respostas = []
indexes = 0
letras = 0
numero_espacamentos = 1
while True:
    
    if soma + len(texto[indexes]) < espacamento:
        letras += len(texto[indexes])
        # print(len(texto[indexes]))
        soma += len(texto[indexes])+1
        espacos+=1
        indexes+=1
        try:
            if soma+len(texto[indexes]) + 1 + len(texto[indexes+1]) <= espacamento:
                numero_espacamentos+=1
        except:
            pass
    elif soma + len(texto[indexes]) == espacamento:
        soma += len(texto[indexes])  
        letras += len(texto[indexes])
        # print(len(texto[indexes]))
        indexes+=1  
    else:

        espacos += espacamento - soma

        try:
            respostas.append(f'{(espacamento - letras)/numero_espacamentos:.3f}')
        except ZeroDivisionError:
            respostas.append(f'0.000')
        # print(espacamento,'\n',letras)
        letras = 0
        numero_espacamentos = 1
        soma = 0
        espacos = 0
    if indexes == len(texto):
        break
    # print(indexes)
numero_letras = 0
indexes_reverso = -1
n_e = 0
if soma != 0:
    while True:
        if numero_letras == soma:
            break
        if numero_letras + len(texto[indexes_reverso]) <= soma:
            numero_letras+=len(texto[indexes_reverso])
            if numero_letras + 1 + len(texto[indexes_reverso-1]) <=soma:
                n_e +=1
                
        indexes_reverso-=1
    try:
        respostas.append(f'{(espacamento - letras)/n_e:.3f}')
    except ZeroDivisionError:
        respostas.append(f'0.000')    
        

print(*respostas)
