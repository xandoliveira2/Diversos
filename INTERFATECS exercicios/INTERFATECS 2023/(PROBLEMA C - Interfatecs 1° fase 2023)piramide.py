#piramide
#input:
#primeira linha é numero e dps separado do tipo
def main():
    con = input().strip().split(' ')
    abc= 'abcdefghijklmnopqrstuvwxyz'
    res = list('.'*26)
    for i in range(0,int(con[0])):
        res.append(abc[i])
        res.remove('.')
        if con[1].lower() == 'maiusculas':
            print (''.join(res).upper())
        else:
            print (''.join(res).lower())
main()
