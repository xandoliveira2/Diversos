#palindromo perdido

def main():
    texto = input().lower()
    textoformatado = str()
    textoreverso = list('-'*len(texto))
    for i in texto:
        if 'á' in i or 'â' in i or'ã' in i or'à' in i:
            textoformatado+='a'
        elif 'ê' in i or'é' in i or'è' in i:
            textoformatado+='e'
        elif i in 'íìî':
            textoformatado+='i'
        elif i in 'óòôõ' :
            textoformatado+='o'
        elif i in 'úùû':
            textoformatado+='u'
        else:
            textoformatado+=i
    for i in textoformatado:
        textoreverso.insert(-1,i)
        textoreverso.remove('-')
    if textoformatado == ''.join(textoreverso):
        print("Parabens, voce encontrou o Palindromo Perdido!")
    else:
        print("A busca continua, o Palindromo Perdido ainda nao foi encontrado.")
        
#ops, esqueci que o encerramento tem que ser com EOF

def main1():
    lista = list()
    while True:
        entrada = input().strip().lower()
        if entrada.lower() == 'eof':
            break
        else:
            lista.append(entrada)
    listanormalizada = list()
    for frase in lista:
        palavranormalizada = ''
        for letra in frase:
            if letra in 'áâãà':
                palavranormalizada+='a'
            elif letra in 'êéè':
                palavranormalizada+='e'
            elif letra in 'íìî':
                palavranormalizada+='i'
            elif letra in ' -_=+!?",\'':
                pass
            elif letra in 'óòôõ' :
                palavranormalizada+='o'
            elif letra in 'úùû':
                palavranormalizada+='u'
            else:
                palavranormalizada+=letra
        formatacao = list(palavranormalizada)
        try:
            if formatacao[-1]== '.':
                formatacao.pop(-1)
        except:
            pass
        palavranormalizada = ''.join(formatacao)
        listanormalizada.append(palavranormalizada)
    listareversa = list()
    for frase in listanormalizada:
        palavrareversa = []
        for letra in frase:
            palavrareversa.insert(0,letra)
        listareversa.append(''.join(palavrareversa))
    for i in range(0,len(listanormalizada)):
        
        if listanormalizada[i] == listareversa[i]:
            print("Parabens, voce encontrou o Palindromo perdido!")
        else:
            print("A busca continua, o Palindromo Perdido ainda nao foi encontrado.")
main1()