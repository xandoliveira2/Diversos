# def main():
# 	lista = []
# 	contador = 0
# 	letra = ''
# 	letras= ''
# 	while True:
# 		entrada = input()
# 		if contador !=1:
# 			letras += entrada[0:3]
# 			contador = 1
# 		if entrada == '':
# 			break
# 		else:
# 			lista.append(list(entrada))
# 	letras = list(letras)
# 	if letras.count(letras[0]) == 1:
# 		letra = letras[1]
# 	else:
# 		letra = letras[0]
# 	for i in range(0,len(lista)):
# 		for j in range(0,len(lista[0])):
# 			if lista[i][j] != letra:
# 				print(f'LINHA {i+1} COLUNA {j+1}')
# 				quit()   
# main()


def verificar(lista):
      if lista[0] == lista[1] and lista[0]== lista[2]:      
            for item in lista:
                  if item != lista[0]:
                        return lista.index(item)+1
      elif lista[0]!=lista[1] and lista[0]==lista[2]:	
            return 2
      elif lista[0]==lista[1] and lista[0]!=lista[2]:	
            return 3
      elif lista[0]!=lista[2] and lista[0]!=lista[2]:	
            return 1
      else:
            return None
def main():
      linha = 1
      while True:
            entrada = input()
            a = verificar(entrada)
            if a:
                  coluna = int(a)
                  print(f'LINHA {linha} COLUNA {coluna}') 
                  break
            linha +=1
main()