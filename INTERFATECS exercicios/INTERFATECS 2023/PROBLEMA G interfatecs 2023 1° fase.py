def main():
    forca = int(input())
    dimensoesy_x = input().split() #ordem de y - x
    y = int(dimensoesy_x[0])
    #x = int(dimensoesy_x[1])
    campo = []
    indexobjetivo = []
    for i in range(0,y):
        linhas = input().strip()
        campo.append(list(linhas.split(' ')))
    for i in campo:
        for j in i:
            if str(j).upper() == 'K':
                indexobjetivo.append(campo.index(i))
                indexobjetivo.append(i.index(j))

    indexinicial_caminho = [0,0]
   # while True:
     #   for i in range(0,y):
            
        






#main()
matriz = [[0,1,'#'],
          [3,'#',5],
          [6,'k',8]]

cont = 0
while cont < len(matriz):
    cont2 = 0
    while cont2 < len(matriz[0]):
        try:
            if matriz[cont][cont2+1]=='#':
                cont2-=1
                pass
            if matriz[cont+1][cont2]=='#':
                
                cont-=1
                pass
            if matriz[cont][cont2]=='k': 
                print('Chegou')
                quit()
        except:
            pass
        print(matriz[cont][cont2])
        cont2+=1
        if cont2> 30:
            break
        

    cont+=1
    if cont > 30:
        break
