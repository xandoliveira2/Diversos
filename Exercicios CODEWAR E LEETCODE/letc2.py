def separacao(x:str):
    x = x.lower()
    lv = []
    cont = 0
    for i in x:
        if i not in lv:
            lv.append(i)
            if cont > len(lv):
                pass
            else:
                cont = len(lv)
        elif i in lv:
            lv.clear()
            lv.append(i)
    print(cont)
ms = 'pwwkew'
separacao(ms)