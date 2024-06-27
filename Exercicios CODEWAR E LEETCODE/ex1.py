


def to_camel_case(text:str):

    if '-' in text and '_' in text:
        newlist = list(text.split('-'))
        newlist1 = list()
        for i in newlist:
            newlist1.append(i.split('_'))
        
        novalista = list()
        cont = 0
        for i in newlist1:
            for j in i:
                if cont == 0:
                    novalista.append(j)
                    cont = 1
                else:
                    novalista.append(j.capitalize())
        string = ''.join(novalista)
        return string
    elif '-' in text:
        newlist = list(text.split('-'))
        newstring = str()
        cont= 0
        for i in newlist:
            if cont==0:
                newstring += i
                cont = 1
            else:
                newstring += i.capitalize()
        return newstring
    elif '_' in text:
        newlist = list(text.split('_'))
        newstring = str()
        cont= 0
        for i in newlist:
            if cont==0:
                newstring += i
                cont = 1
            else:
                newstring += i.capitalize()
        return newstring
    elif text == '':
        return ''

def teste(text:str):
    if text=='':
        return ''
    else:
        minhastr = text.replace('-',' ').replace('_',' ')
        minhalista = list(minhastr.split(' '))
        minhanovastr = str()
        cont = 0
        for i in minhalista:
            if cont == 0:
                minhanovastr += i
                cont=1
            else:
                minhanovastr+=i.capitalize()
        return minhanovastr
