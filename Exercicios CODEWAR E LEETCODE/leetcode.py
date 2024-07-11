def ex2(x:list,y:list):
    c = []
    d = str()
    f = str()
    x.reverse()
    y.reverse()
    for i in x:
        i = str(i)
        d = d+i
    for i in y:
        i = str(i)
        f = f+i
    c.append(d)
    c.append(f)
    e = str(int(c[0])+int(c[1]))
    c.clear()
    for i in e:
        c.append(int(i))
    c.reverse()
    print(c)
l1 = [2,4,3]
l2 =[5,6,4]
ex2(l1,l2)