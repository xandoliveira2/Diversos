
def main():
    bochas_turnos = input().split(' ')
    bochas = int(bochas_turnos[0])
    turnos = int(bochas_turnos[1])
    whites = []
    reds = []
    for i in range(0,turnos): # 3 2 
        bolim = input().split(' ')
        for white in range(0,bochas): 
            leitor = input().split(' ')
            x_bolim = int(bolim[0])
            y_bolim = int(bolim[1])
            x_bocha = int(leitor[0])
            y_bocha = int(leitor[1])
            a = (x_bocha - x_bolim)**2 + (y_bocha - y_bolim)**2
            distancia = a**(1/2)

            whites.append(distancia)
        for red in range(0,bochas):
            # leitor = input().split(' ')
            # distancia = (((int(leitor[0]) - int(bolim[0]))**2) + (int(leitor[1]) - int(bolim[1])))**0.5
            leitor = input().split(' ')
            x_bolim = int(bolim[0])
            y_bolim = int(bolim[1])
            x_bocha = int(leitor[0])
            y_bocha = int(leitor[1])
            a = (x_bocha - x_bolim)**2 + (y_bocha - y_bolim)**2
            distancia = a**(1/2)
            reds.append(distancia)
    
    print(whites,reds)
    
   


#     dist = (((x_b - y_b)**2)+((x_j-y_j)**2))**1/2

                
        
            


    print(f"PONTOS DAS BOCHAS BRANCAS = ")
    print(f"PONTOS DAS BOCHAS VERMELHAS = ")
    



        



main()