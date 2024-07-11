import os
os.system('cls')
class romano:
    roman = {'M': 1000,
             'D': 500,
             'C': 100,
             'L': 50,
             'X': 10,
             'V': 5,
             'I': 1,
             }
    def pegar(x:str):
        num = 0
        
        for i in x:
            for c in romano.roman:
                if i.upper() == c.upper():
                    num += romano.roman.get(c)
        return int(num)
           
sla = 'xxxi'
print(romano.pegar(sla))