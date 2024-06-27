def cakes(recipe:dict, available:dict):
    lista = list(recipe.keys())
    cont = 0
    oli=[]
    menor = 99999999999999999999
    l = []
    for i in range(0,len(recipe)):
        if recipe.get(str(lista[i])) < int(available.get(str(lista[i]))):
            cont = available.get(lista[i]) // recipe.get(lista[i]) 
            oli.append(cont)
        else:
            return 0
    
    for j in oli:
        if int(j) < menor:
            menor = int(j)
    return menor


recipe = {'flour': 500, 'sugar': 200, 'eggs': 1}
disponivel ={'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}

print(cakes(recipe,disponivel))


recipe1 = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
disponivel1 = {'sugar': 500, 'flour': 2000, 'milk': 2000}
print(cakes(recipe1,disponivel1))