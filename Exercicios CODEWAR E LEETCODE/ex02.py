def reverter(x:str):
    varlocal = list('-'*len(x))
    for i in x:
        varlocal.insert(0,i)
        varlocal.remove('-')
    
    return ''.join(varlocal)

def main(x:str):
    var = x.split(' ')
    resposta = []
    for i in var:
        if len(i)>=5:
            resposta.append(reverter(i))
        else:
            resposta.append(i)
    return ' '.join(resposta)


