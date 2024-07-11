def sumarays(a:list,b:list):
    c = a + b
    cal = int()
    for i in c:
        cal = cal + i
    cal = cal / len(c)
    print(cal)
l1 = [1,2]
l2 = [3,4]
sumarays(l1,l2)