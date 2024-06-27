#criptografia cesar
#tabelanormal = a b c d e f g h i j k l m n o p q r s t u v w x y z
#tabelacripto = d e f g h i j k l m n o p q r s t u v w x y z a b c

cripto = {1 : 'd',
        2 :'e',
        3 :'f',
        4 :'g',
        5 :'h',
        6 :'i',
        7 :'j',
        8 :'k',
        9 :'l',
        10:'m',
        11:'n',
        12:'o',
        13:'p',
        14:'q',
        15:'r',
        16:'s',
        17:'t',
        18:'u',
        19:'v',
        20:'w',
        21:'x',
        22:'y',
        23:'z',
        24:'a',
        25:'b',
        26:'c'
          }

palavra = 'matematica genial'
def conversao(p:str):
    gabarito = 'abcdefghijklmnopqrstuvwxyz'
    index = int()
    msgcriptografada = []
    for i in p:
        for j in gabarito:
            if j.lower() == i.lower():
                index= gabarito.index(j)+1
        msgcriptografada.append(cripto.get(index))
    return ''.join(msgcriptografada)
print(conversao(palavra))