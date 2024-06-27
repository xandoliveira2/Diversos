def pig_it(text:str):
    palavras = text.split(' ')
    nt = []
    
    for palavra in palavras:
        cont = 0
        guardar = str()
        actstr = str()
        if '!' in palavra:
            nt.append(palavra)
            pass
        else:

            for letra in palavra:
            
                if cont ==0:
                    guardar = letra+'ay'
                    cont = 1
                else:
                    actstr+=letra
            actstr +=guardar
            nt.append(actstr)
    print(nt)
    print(palavras)
    return ' '.join(nt)
