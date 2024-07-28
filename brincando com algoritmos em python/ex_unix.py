DIA = 60*60*24 #segundos por dia -> 86400
ANO_INICIO = 1970

def bissexto(ano:int) -> bool:
    if ano % 4 == 0:
        return True
    return False
def unixtime(data:str='01/01/2024',horario:str='00:00:00',UTC:int = 3) -> int:
    meses = {2:28,4:30,6:30,9:30,11:30}
    tempo=0
    data = data.split('/')
    diastotais = 0
    for i in range(ANO_INICIO,int(data[2])):
        if bissexto(i):
            diastotais+=366
        else:
            diastotais+=365 
    for i in range(1,int(data[1])):
        if i == 2 and bissexto(int(data[2])):
            diastotais+= meses.get(i)+1
        elif i in meses.keys():
            diastotais+= meses.get(i)

        else:
            diastotais+=31
 
    diastotais += int(data[0])-1
    
    tempo = diastotais * DIA

    horario = horario.split(':')

    for i in range(len(horario)):
        if i == 0:
            tempo += ((int(horario[i])+UTC) * 60) * 60
        elif i == 1:
            tempo += int(horario[i]) * 60
        elif i == 2:
            tempo += int(horario[i])
            
    return tempo
# print(unixtime('28/07/2024','15:08'))
def formatar(horas:int,minutos:int) -> str:
    if horas<10:
        return str(f'0{horas}:0{minutos}')
    else:
        return str(f'{horas}:{minutos}')
def tempoiguais(data:str='01/01/2024') -> list[(str,int)]:
    
    timeunix = unixtime(data)
    lista =[('00:00',timeunix)]
    horas,minutos = 1,1
    while horas < 24 and minutos < 24:
        lista.append((formatar(horas,minutos),unixtime(data,formatar(horas,minutos))))
        horas+=1
        minutos+=1

    return lista


print(tempoiguais('28/07/2024'))












# # from operator import itemgetter, attrgetter
# # palavra = 'sopa de macaco'
# # dic = {}
# # for i in palavra:
# #     try:
# #         dic[i] +=1
# #     except:
# #         dic[i]=1
# # print(dic)
# # dic = sorted(dic,key= lambda a : dic[a],reverse=True)
# # print(dic)







# # a =[1,2,3,4,5,6,7,8,9,10]

# # print(list(map((lambda i: i*i),a)))
# # contador = 0
# # print(contador)
# # milhao = 1000000
# # bilhao = 1000000000
# # trilhao = 1000000000000
# # number = 0
# # import time
# # comeco = time.time()
# # for i in range(milhao):
# #     number+=i
# # fim = time.time()
# # print(f'{fim-comeco}.../...milhoes:{number//milhao}')


#  # ex: inverter 274 para 472 sem usar str, apenas matematica (nem sei se é possivel)
# ##codigo abaixo pego do chatgpt, sem méritos
# from time import time
# comeco1 = time()
# def inverter_numero(numero):
#     invertido = 0
#     while numero != 0: #exemplo primeiro loop                           
#         digito = numero % 10 # digito = 274 % 10 -> digito =  4                                                 digito = 27  % 10 -> digito = 7    
#         print(digito)
#         invertido = invertido * 10 + digito # invertido = 0 * 10 + 4 -> invertido = 4                           invertido = 4 * 10 + 7 -> invertido = 47  
#         print(invertido)
#         numero = numero // 10 # numero = 274 //10 -> numero = 27                                                numero = 27 // 10 -> numero = 2
#         print(numero)
#     return invertido

# numero = 318
# fim1 = time()

# comeco2 = time()
# numero = 318
# fim2 = time()
# if (fim2-comeco2) < (fim1-comeco1):
#     print("metodo de string melhor")
# else:
#     print("metodo matematico melhor")
# # conclusão -> numeros menores os dois são 'instantaneos' porém com maiores é muito mais vantajoso usar em string mesmo


