#pegar varios palindromos e escrever se é um palindromo ou nao
def main():
    valores = list()
    newlist = list()
    newlist1= list()
    newlistr=list()
    newlistf = list()
    mstr = str()
    while True:
        f = input().strip()
        if f.upper() == "EOF":
            break
        else:
            valores.append(f)
    for i in valores:
        mstr = ""
        for j in i: 
            if j == ' ':
                pass
            else:
                mstr += j
            if j == j[-1]:
                newlist.append(mstr)
        newlist1.append(newlist[-1])
        for i in newlist1:
            newlistr = []
            for j in i:
                newlistr.insert(0,j)
            mstr = ''.join(newlistr)
            if mstr in newlistf:
                pass
            else:
                newlistf.append(mstr)
    for i in range(0,len(newlist1)):
        if newlist1[i] == newlistf[i]:
            print('Palindromo')
        else:
            print('nâo é um palindromo')
main()